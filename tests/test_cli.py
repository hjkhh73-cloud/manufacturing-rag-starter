import csv
import json
import tempfile
import unittest
from pathlib import Path

from mfg_rag_starter.cli import build_jsonl, normalize_tags, preview_jsonl


class CliTests(unittest.TestCase):
    def test_normalize_tags_supports_semicolon_variants(self):
        self.assertEqual(normalize_tags("ERP; MES；WMS"), ["ERP", "MES", "WMS"])

    def test_build_and_preview_jsonl(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "knowledge.csv"
            output = root / "knowledge.jsonl"
            with source.open("w", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["id", "title", "scenario", "source_type", "tags", "content"],
                )
                writer.writeheader()
                writer.writerow(
                    {
                        "id": "KB-001",
                        "title": "Work order reporting",
                        "scenario": "MES",
                        "source_type": "SOP",
                        "tags": "MES;work order",
                        "content": "Operators report quantity, scrap, machine, and time.",
                    }
                )

            count = build_jsonl(source, output)
            self.assertEqual(count, 1)
            records = preview_jsonl(output, 1)
            self.assertEqual(records[0]["id"], "KB-001")
            self.assertIn("Work order reporting", records[0]["text"])
            self.assertEqual(records[0]["tags"], ["MES", "work order"])
            json.loads(output.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
