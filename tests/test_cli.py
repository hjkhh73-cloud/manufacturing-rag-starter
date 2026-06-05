import csv
import json
import tempfile
import unittest
from pathlib import Path

from mfg_rag_starter.cli import (
    build_jsonl,
    evaluate_retrieval,
    export_markdown,
    normalize_tags,
    preview_jsonl,
    safe_filename,
    write_evaluation_report,
)


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

    def test_evaluate_retrieval_reports_expected_source_hit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            knowledge = root / "knowledge.jsonl"
            questions = root / "questions.jsonl"
            output = root / "results.json"
            knowledge.write_text(
                json.dumps(
                    {
                        "id": "KB-WMS-001",
                        "text": "WMS inventory mismatch material code warehouse batch number",
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            questions.write_text(
                json.dumps(
                    {
                        "id": "EVAL-WMS-001",
                        "question": "Which fields identify a WMS inventory mismatch?",
                        "expected_source_ids": ["KB-WMS-001"],
                    }
                )
                + "\n",
                encoding="utf-8",
            )

            report = evaluate_retrieval(knowledge, questions)
            self.assertEqual(report["hits"], 1)
            self.assertEqual(report["score"], 1)

            written = write_evaluation_report(knowledge, questions, output)
            self.assertEqual(written["metric"], "hit@1")
            self.assertEqual(json.loads(output.read_text(encoding="utf-8"))["hits"], 1)

    def test_export_markdown_creates_upload_ready_document(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "knowledge.csv"
            output_dir = root / "documents"
            with source.open("w", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["id", "title", "scenario", "source_type", "tags", "content"],
                )
                writer.writeheader()
                writer.writerow(
                    {
                        "id": "KB/WMS 001",
                        "title": "Inventory mismatch",
                        "scenario": "WMS/MES",
                        "source_type": "SOP",
                        "tags": "WMS;MES",
                        "content": "Collect material code and batch number.",
                    }
                )

            self.assertEqual(export_markdown(source, output_dir), 1)
            document = output_dir / "KB_WMS_001.md"
            self.assertTrue(document.exists())
            self.assertIn('id: "KB/WMS 001"', document.read_text(encoding="utf-8"))
            self.assertIn("# Inventory mismatch", document.read_text(encoding="utf-8"))

            self.assertEqual(export_markdown(source, output_dir), 1)
            document.write_text("changed", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                export_markdown(source, output_dir)

    def test_safe_filename_removes_path_characters(self):
        self.assertEqual(safe_filename("../KB/WMS 001"), "KB_WMS_001")

    def test_evaluate_retrieval_rejects_invalid_top_k(self):
        with self.assertRaises(ValueError):
            evaluate_retrieval(Path("knowledge.jsonl"), Path("questions.jsonl"), 0)


if __name__ == "__main__":
    unittest.main()
