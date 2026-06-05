import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_jsonl(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


class EvaluationDataTests(unittest.TestCase):
    def test_evaluation_cases_reference_existing_knowledge(self):
        knowledge = read_jsonl(ROOT / "examples" / "manufacturing_kb.jsonl")
        questions = read_jsonl(ROOT / "evaluation" / "manufacturing_eval_questions.jsonl")
        knowledge_ids = {item["id"] for item in knowledge}

        self.assertGreaterEqual(len(questions), 10)
        for case in questions:
            self.assertTrue(case["id"].startswith("EVAL-"))
            self.assertTrue(case["category"])
            self.assertTrue(case["question"])
            self.assertTrue(case["expected_answer_points"])
            self.assertTrue(case["risk_if_wrong"])
            self.assertTrue(set(case["expected_source_ids"]).issubset(knowledge_ids))


if __name__ == "__main__":
    unittest.main()
