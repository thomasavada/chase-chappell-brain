#!/usr/bin/env python3
"""Report unindexed Chase Chappell videos and Shorts as stable JSON.

The knowledge markdown is the source of truth: a video is indexed when its
11-character YouTube ID appears anywhere under knowledge/. This script only
discovers work. A scheduled Hermes agent distils the transcript and edits the
brain; raw transcripts are never stored in the repository.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = REPO_ROOT / "plugins/chase-chappell-knowledge/knowledge"
CHANNEL = "https://www.youtube.com/@ChaseChappell"
VIDEO_ID_RE = re.compile(
    r"(?:youtu\.be/|youtube\.com/(?:watch\?(?:[^\s)]*&)?v=|shorts/))"
    r"([A-Za-z0-9_-]{11})"
)


def indexed_video_ids(knowledge_dir: Path = KNOWLEDGE_DIR) -> set[str]:
    """Return every YouTube ID cited by the current knowledge corpus."""
    ids: set[str] = set()
    for note in knowledge_dir.rglob("*.md"):
        ids.update(VIDEO_ID_RE.findall(note.read_text(encoding="utf-8")))
    return ids


def fetch_tab(kind: str, limit: int) -> list[dict[str, Any]]:
    """Fetch a channel tab without downloading media."""
    yt_dlp = shutil.which("yt-dlp")
    if not yt_dlp:
        raise RuntimeError("yt-dlp is not installed or is not on PATH")

    result = subprocess.run(
        [
            yt_dlp,
            "--flat-playlist",
            "--playlist-end",
            str(limit),
            "--dump-single-json",
            f"{CHANNEL}/{kind}",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=300,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"yt-dlp failed for {kind}")

    payload = json.loads(result.stdout)
    items: list[dict[str, Any]] = []
    for entry in payload.get("entries") or []:
        video_id = entry.get("id")
        title = entry.get("title")
        if not video_id or not title:
            continue
        items.append(
            {
                "id": video_id,
                "kind": "short" if kind == "shorts" else "video",
                "title": title,
                "url": (
                    f"https://www.youtube.com/shorts/{video_id}"
                    if kind == "shorts"
                    else f"https://www.youtube.com/watch?v={video_id}"
                ),
            }
        )
    return items


def pending_items(limit: int) -> list[dict[str, Any]]:
    indexed = indexed_video_ids()
    seen: set[str] = set()
    pending: list[dict[str, Any]] = []
    for kind in ("videos", "shorts"):
        for item in fetch_tab(kind, limit):
            video_id = item["id"]
            if video_id not in indexed and video_id not in seen:
                pending.append(item)
                seen.add(video_id)
    return pending


def main() -> int:
    parser = argparse.ArgumentParser(
        description="List recent Chase Chappell uploads missing from the brain"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="number of recent items to inspect on each channel tab (default: 10)",
    )
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be at least 1")

    try:
        pending = pending_items(args.limit)
    except (RuntimeError, json.JSONDecodeError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False, sort_keys=True))
        return 1

    print(
        json.dumps(
            {"pending": pending, "pending_count": len(pending)},
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())