from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class KnowledgeRecord:
    """A single manufacturing knowledge record prepared for RAG ingestion."""

    id: str
    title: str
    scenario: str
    source_type: str
    tags: list[str]
    content: str


def normalize_tags(value: str) -> list[str]:
    return [item.strip() for item in value.replace("；", ";").split(";") if item.strip()]


def read_csv(path: Path) -> Iterable[KnowledgeRecord]:
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        required = {"id", "title", "scenario", "source_type", "tags", "content"}
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
        for row in reader:
            yield KnowledgeRecord(
                id=row["id"].strip(),
                title=row["title"].strip(),
                scenario=row["scenario"].strip(),
                source_type=row["source_type"].strip(),
                tags=normalize_tags(row["tags"]),
                content=row["content"].strip(),
            )


def to_rag_document(record: KnowledgeRecord) -> dict:
    text = (
        f"# {record.title}\n\n"
        f"Scenario: {record.scenario}\n"
        f"Source type: {record.source_type}\n"
        f"Tags: {', '.join(record.tags)}\n\n"
        f"{record.content}\n"
    )
    return {
        "id": record.id,
        "title": record.title,
        "scenario": record.scenario,
        "source_type": record.source_type,
        "tags": record.tags,
        "text": text,
        "metadata": asdict(record),
    }


def build_jsonl(input_path: Path, output_path: Path) -> int:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with output_path.open("w", encoding="utf-8") as out:
        for record in read_csv(input_path):
            out.write(json.dumps(to_rag_document(record), ensure_ascii=False) + "\n")
            count += 1
    return count


def preview_jsonl(input_path: Path, limit: int) -> list[dict]:
    results: list[dict] = []
    with input_path.open("r", encoding="utf-8") as file:
        for line in file:
            if len(results) >= limit:
                break
            results.append(json.loads(line))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Manufacturing RAG Starter CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    build_parser = subparsers.add_parser("build", help="Build JSONL knowledge records from a CSV file")
    build_parser.add_argument("--input", required=True, type=Path, help="Input CSV file")
    build_parser.add_argument("--output", required=True, type=Path, help="Output JSONL file")

    preview_parser = subparsers.add_parser("preview", help="Preview generated JSONL records")
    preview_parser.add_argument("--input", required=True, type=Path, help="Input JSONL file")
    preview_parser.add_argument("--limit", default=3, type=int, help="Number of records to preview")

    args = parser.parse_args()
    if args.command == "build":
        count = build_jsonl(args.input, args.output)
        print(f"Generated {count} RAG records: {args.output}")
    elif args.command == "preview":
        for item in preview_jsonl(args.input, args.limit):
            print(json.dumps(item, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
