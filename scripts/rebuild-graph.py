#!/usr/bin/env python3
"""Rebuild the committed wikilink graph without an external Graphify install."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = REPO_ROOT / "plugins/chase-chappell-knowledge/knowledge"
OUT_DIR = REPO_ROOT / "graphify-out"
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")
SLUG_RE = re.compile(r"[^a-z0-9]+")
COLORS = ["#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F", "#EDC948", "#B07AA1"]
COMMUNITY_NAMES = {
    0: "Andromeda + 4-campaign",
    1: "Positioning + offer",
    2: "Diagnosis + site LTV",
    3: "AI creative stack",
    4: "Funnel + scale sources",
    5: "TikTok Shop army",
    6: "Hub + Euka army",
}


def note_id(label: str) -> str:
    return "note_" + SLUG_RE.sub("_", label.casefold()).strip("_")


def load_previous_communities() -> dict[str, int]:
    graph_path = OUT_DIR / "graph.json"
    if not graph_path.exists():
        return {}
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    return {node["label"].casefold(): int(node.get("community", 0)) for node in graph["nodes"]}


def load_previous_graph() -> dict[str, Any] | None:
    graph_path = OUT_DIR / "graph.json"
    if not graph_path.exists():
        return None
    return json.loads(graph_path.read_text(encoding="utf-8"))


def edge_key(edge: dict[str, Any]) -> tuple[str, str]:
    ordered = sorted((edge["source"], edge["target"]))
    return (ordered[0], ordered[1])


def graph_signature(graph: dict[str, Any]) -> tuple[frozenset[str], frozenset[tuple[str, str]]]:
    return (
        frozenset(node["id"] for node in graph["nodes"]),
        frozenset(edge_key(edge) for edge in graph["links"]),
    )


def preserve_existing_order(graph: dict[str, Any], previous: dict[str, Any] | None) -> dict[str, Any]:
    """Keep stable JSON ordering so one new note creates a small graph diff."""
    if not previous:
        return graph
    new_nodes = {node["id"]: node for node in graph["nodes"]}
    ordered_nodes = [new_nodes.pop(node["id"]) for node in previous["nodes"] if node["id"] in new_nodes]
    ordered_nodes.extend(new_nodes.values())

    new_links = {edge_key(edge): edge for edge in graph["links"]}
    ordered_links = []
    for edge in previous["links"]:
        key = edge_key(edge)
        if key in new_links:
            ordered_links.append(edge)
            new_links.pop(key)
    ordered_links.extend(new_links.values())
    return {**graph, "nodes": ordered_nodes, "links": ordered_links}


def build_graph() -> tuple[dict[str, Any], list[str]]:
    files = sorted(KNOWLEDGE_DIR.rglob("*.md"), key=lambda path: path.relative_to(KNOWLEDGE_DIR).as_posix())
    by_label = {path.stem.casefold(): path for path in files}
    old_communities = load_previous_communities()
    edge_sources: dict[tuple[str, str], str] = {}
    unresolved: set[str] = set()
    neighbors: dict[str, set[str]] = defaultdict(set)

    for path in files:
        source_label = path.stem
        source_rel = path.relative_to(KNOWLEDGE_DIR).as_posix()
        for raw_target in WIKILINK_RE.findall(path.read_text(encoding="utf-8")):
            target_label = raw_target.strip()
            target_path = by_label.get(target_label.casefold())
            if not target_path:
                unresolved.add(target_label)
                continue
            target_label = target_path.stem
            if source_label == target_label:
                continue
            ordered = sorted((source_label, target_label), key=str.casefold)
            pair = (ordered[0], ordered[1])
            edge_sources.setdefault(pair, source_rel)
            neighbors[source_label].add(target_label)
            neighbors[target_label].add(source_label)

    communities = dict(old_communities)
    for path in files:
        label = path.stem
        if label.casefold() in communities:
            continue
        votes = Counter(
            communities[neighbor.casefold()]
            for neighbor in neighbors[label]
            if neighbor.casefold() in communities
        )
        communities[label.casefold()] = votes.most_common(1)[0][0] if votes else 0

    nodes = []
    for path in files:
        label = path.stem
        community = communities[label.casefold()]
        nodes.append(
            {
                "label": label,
                "file_type": "document",
                "source_file": path.relative_to(KNOWLEDGE_DIR).as_posix(),
                "source_location": None,
                "_origin": "extracted",
                "id": note_id(label),
                "community": community,
                "norm_label": label.casefold(),
            }
        )

    links = []
    for (left, right), source_file in sorted(edge_sources.items(), key=lambda item: tuple(part.casefold() for part in item[0])):
        links.append(
            {
                "relation": "wikilink",
                "confidence": "EXTRACTED",
                "confidence_score": 1.0,
                "source_file": source_file,
                "source_location": None,
                "weight": 1.0,
                "_origin": "extracted",
                "source": note_id(left),
                "target": note_id(right),
            }
        )

    graph = {"directed": False, "multigraph": False, "graph": {}, "nodes": nodes, "links": links}
    return preserve_existing_order(graph, load_previous_graph()), sorted(unresolved)


def update_manifest() -> None:
    manifest_path = OUT_DIR / "manifest.json"
    previous = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    manifest = {}
    for path in sorted(KNOWLEDGE_DIR.rglob("*.md")):
        content = path.read_bytes()
        digest = hashlib.md5(content).hexdigest()
        relative = path.relative_to(KNOWLEDGE_DIR).as_posix()
        old_entry = previous.get(relative)
        if old_entry and old_entry.get("semantic_hash") == digest:
            manifest[relative] = old_entry
        else:
            manifest[relative] = {
                "mtime": path.stat().st_mtime,
                "ast_hash": digest,
                "semantic_hash": digest,
            }
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def update_report(graph: dict[str, Any]) -> None:
    degrees = Counter()
    for edge in graph["links"]:
        degrees[edge["source"]] += 1
        degrees[edge["target"]] += 1
    labels = {node["id"]: node["label"] for node in graph["nodes"]}
    word_count = sum(len(path.read_text(encoding="utf-8").split()) for path in KNOWLEDGE_DIR.rglob("*.md"))
    communities: dict[int, list[str]] = defaultdict(list)
    for node in graph["nodes"]:
        communities[node["community"]].append(node["label"])

    lines = [
        f"# Graph Report - {KNOWLEDGE_DIR}  ({date.today().isoformat()})",
        "",
        "## Corpus Check",
        f"- {len(graph['nodes'])} files · ~{word_count:,} words",
        "- Verdict: corpus is large enough that graph structure adds value.",
        "",
        "## Summary",
        f"- {len(graph['nodes'])} nodes · {len(graph['links'])} edges · {len(communities)} communities",
        "- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS",
        "- Token cost: 0 input · 0 output",
        "",
        "## God Nodes (most connected - your core abstractions)",
    ]
    for rank, (node_id, degree) in enumerate(degrees.most_common(10), start=1):
        lines.append(f"{rank}. `{labels[node_id]}` - {degree} edges")
    lines.extend(["", f"## Communities ({len(communities)} total)", ""])
    for community in sorted(communities):
        members = sorted(communities[community], key=str.casefold)
        name = COMMUNITY_NAMES.get(community, f"Community {community}")
        preview = ", ".join(members[:8])
        if len(members) > 8:
            preview += f" (+{len(members) - 8} more)"
        lines.extend([f"### Community {community} - \"{name}\"", f"Nodes ({len(members)}): {preview}", ""])
    (OUT_DIR / "GRAPH_REPORT.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def update_html(graph: dict[str, Any]) -> None:
    html_path = OUT_DIR / "graph.html"
    if not html_path.exists():
        return
    html = html_path.read_text(encoding="utf-8")
    degrees = Counter()
    for edge in graph["links"]:
        degrees[edge["source"]] += 1
        degrees[edge["target"]] += 1

    raw_nodes = []
    community_counts = Counter(node["community"] for node in graph["nodes"])
    for node in graph["nodes"]:
        community = node["community"]
        degree = degrees[node["id"]]
        color = COLORS[community % len(COLORS)]
        raw_nodes.append(
            {
                "id": node["id"],
                "label": node["label"],
                "color": {"background": color, "border": color, "highlight": {"background": "#ffffff", "border": color}},
                "size": round(10 + math.sqrt(degree) * 2.65, 1),
                "font": {"size": 12 if degree >= 8 else 0, "color": "#ffffff"},
                "title": node["label"],
                "community": community,
                "community_name": COMMUNITY_NAMES.get(community, f"Community {community}"),
                "source_file": node["source_file"],
                "file_type": "document",
                "degree": degree,
            }
        )
    raw_edges = [
        {
            "from": edge["source"],
            "to": edge["target"],
            "label": "wikilink",
            "title": "wikilink [EXTRACTED]",
            "dashes": False,
            "width": 2,
            "color": {"opacity": 0.7},
            "confidence": "EXTRACTED",
        }
        for edge in graph["links"]
    ]
    legend = [
        {"cid": cid, "color": COLORS[cid % len(COLORS)], "label": COMMUNITY_NAMES.get(cid, f"Community {cid}"), "count": count}
        for cid, count in sorted(community_counts.items())
    ]
    stats = f"{len(raw_nodes)} nodes &middot; {len(raw_edges)} edges &middot; {len(legend)} communities"
    html = re.sub(r'<div id="stats">.*?</div>', f'<div id="stats">{stats}</div>', html, count=1)
    html = re.sub(r"const RAW_NODES = .*?;\n", "const RAW_NODES = " + json.dumps(raw_nodes, ensure_ascii=False) + ";\n", html, count=1)
    html = re.sub(r"const RAW_EDGES = .*?;\n", "const RAW_EDGES = " + json.dumps(raw_edges, ensure_ascii=False) + ";\n", html, count=1)
    html = re.sub(r"const LEGEND = .*?;\n", "const LEGEND = " + json.dumps(legend, ensure_ascii=False) + ";\n", html, count=1)
    html_path.write_text(html, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Rebuild graphify-out from markdown wikilinks")
    parser.add_argument("--check", action="store_true", help="validate extraction without writing files")
    args = parser.parse_args()
    previous = load_previous_graph()
    graph, unresolved = build_graph()
    if unresolved:
        print("Unresolved wikilinks: " + ", ".join(unresolved))
        return 1
    if args.check:
        print(json.dumps({"nodes": len(graph["nodes"]), "edges": len(graph["links"]), "unresolved": 0}, sort_keys=True))
        return 0

    if previous and graph_signature(previous) == graph_signature(graph):
        print(json.dumps({"edges": len(graph["links"]), "nodes": len(graph["nodes"]), "status": "unchanged", "unresolved": 0}, sort_keys=True))
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "graph.json").write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    update_manifest()
    update_report(graph)
    update_html(graph)

    print(json.dumps({"nodes": len(graph["nodes"]), "edges": len(graph["links"]), "unresolved": 0}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
