# Manufacturing RAG Evaluation Guide

This project includes a small, reusable evaluation set for checking whether a
manufacturing RAG assistant retrieves the expected source records.

## What is evaluated

The evaluation set covers:

- ERP and MES order ownership;
- BOM and MRP exceptions;
- WMS and MES inventory mismatches;
- quality inspection and nonconformance handling;
- delivery commitment;
- manufacturing gross margin analysis.

Each case in
[`evaluation/manufacturing_eval_questions.jsonl`](../evaluation/manufacturing_eval_questions.jsonl)
contains a question, expected source record, expected answer points, and the
business risk of a wrong answer.

## Run the baseline

Build the sample knowledge base and run the deterministic keyword retrieval
baseline:

```bash
python -m mfg_rag_starter build \
  --input data/sample_knowledge.csv \
  --output examples/manufacturing_kb.jsonl

python -m mfg_rag_starter evaluate \
  --knowledge examples/manufacturing_kb.jsonl \
  --questions evaluation/manufacturing_eval_questions.jsonl \
  --output evaluation/baseline_results.json \
  --top-k 1
```

The generated report shows the expected source IDs, retrieved source IDs, and
whether each case was a hit.

## Interpreting the result

This baseline measures source retrieval only. It does **not** claim that an LLM
generated a complete or correct final answer. When evaluating a Dify,
AnythingLLM, or custom RAG assistant, review both:

1. whether the expected source was retrieved;
2. whether the generated answer covers the expected answer points without
   inventing unsupported details.

Use synthetic or anonymized manufacturing data. Do not upload customer
documents, credentials, personal information, or proprietary production data.
