import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("daily-brain-update.py")
SPEC = importlib.util.spec_from_file_location("daily_brain_update", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class IndexedVideoIdsTest(unittest.TestCase):
    def test_extracts_watch_short_and_youtu_be_links(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "note.md").write_text(
                "\n".join(
                    [
                        "https://youtube.com/watch?v=abcdefghijk",
                        "https://www.youtube.com/shorts/lmnopqrstuv",
                        "https://youtu.be/12345678901?t=4",
                    ]
                ),
                encoding="utf-8",
            )

            self.assertEqual(
                MODULE.indexed_video_ids(root),
                {"abcdefghijk", "lmnopqrstuv", "12345678901"},
            )


if __name__ == "__main__":
    unittest.main()