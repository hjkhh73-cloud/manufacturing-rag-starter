# Dify / AnythingLLM Import Guide

This guide explains how to use the generated manufacturing knowledge base with common RAG tools.

## 1. Generate JSONL

```bash
python -m mfg_rag_starter build --input data/sample_knowledge.csv --output examples/manufacturing_kb.jsonl
```

## 2. Generate upload-ready Markdown

Dify and AnythingLLM can ingest plain Markdown documents. Generate one
upload-ready document per synthetic knowledge record:

```bash
python -m mfg_rag_starter export-markdown \
  --input data/sample_knowledge.csv \
  --output-dir examples/upload-ready-markdown
```

The repository already includes the generated example folder:
[`examples/upload-ready-markdown`](../examples/upload-ready-markdown).

The command is safe to run again when generated files are unchanged. It refuses
to overwrite a generated file if that file has been manually changed.

## 3. Dify

Tool interfaces may change between versions. The repeatable workflow is:

1. create a new knowledge base;
2. upload all `.md` files from `examples/upload-ready-markdown`;
3. confirm that five documents were accepted;
4. use the default or balanced chunking option first;
5. create an assistant connected only to this test knowledge base;
6. use the prompt below and run the validation questions.

Suggested test questions:

- How should we handle BOM version changes after a work order has started?
- What information should be collected when MES and WMS inventory records disagree?
- What is the difference between order-level margin and product-line margin?

## 4. AnythingLLM

Repeatable workflow:

1. create a workspace for a manufacturing domain, such as `ERP-MES-WMS Assistant`;
2. upload all `.md` files from `examples/upload-ready-markdown`;
3. move or attach all five documents to the workspace;
4. ask the assistant to cite the source title and scenario;
5. use the prompt below and run the validation questions.

## 5. Prompt suggestion

```text
You are a manufacturing digitalization assistant. Answer with practical steps.
When the question involves ERP, MES, WMS, APS, BOM, MRP, orders, inventory, work orders, quality inspection, delivery, or finance analysis, first identify the business scenario, then provide process steps, required fields, exception handling, and final output.
If information is missing, list the missing fields before giving a recommendation.
```

## 6. Validation checklist

Run these questions after import:

1. What should be checked before a new BOM version becomes effective?
2. What fields should be collected when WMS inventory differs from MES material consumption?
3. Which disposition decisions can follow a failed quality inspection?
4. Which costs should be included in manufacturing gross margin analysis?

For a transparent review, compare the answer with
[`evaluation/manufacturing_eval_questions.jsonl`](../evaluation/manufacturing_eval_questions.jsonl).
Confirm that the answer uses the expected source and covers the expected answer
points. Do not count unsupported or invented details as correct.

## 7. What is and is not verified

Verified by this repository:

- the CSV-to-Markdown export command;
- the five generated synthetic documents;
- file metadata and content generation;
- automated tests and CI.

Not automatically verified by this repository:

- the current Dify or AnythingLLM user-interface labels;
- model-specific answer quality;
- performance with private or production documents.

## 8. Upstream references

- [Dify: Create Knowledge Base](https://docs.dify.ai/en/guides/knowledge-base/create-knowledge-and-upload-documents)
- [Dify: Upload Local Files](https://docs.dify.ai/en/guides/knowledge-base/create-knowledge-and-upload-documents/import-content-data/readme)
- [AnythingLLM documentation](https://docs.anythingllm.com/)
- [AnythingLLM accepted file types](https://github.com/Mintplex-Labs/anything-llm/blob/master/collector/utils/constants.js)
