# Dify / AnythingLLM Import Guide

This guide explains how to use the generated manufacturing knowledge base with common RAG tools.

## 1. Generate JSONL

```bash
python -m mfg_rag_starter build --input data/sample_knowledge.csv --output examples/manufacturing_kb.jsonl
```

## 2. Dify

Recommended approach:

1. create a new knowledge base;
2. upload Markdown files or convert JSONL records into plain text documents;
3. use a balanced chunk size first;
4. test with manufacturing questions before changing model settings.

Suggested test questions:

- How should we handle BOM version changes after a work order has started?
- What information should be collected when MES and WMS inventory records disagree?
- What is the difference between order-level margin and product-line margin?

## 3. AnythingLLM

Recommended approach:

1. create a workspace for a manufacturing domain, such as `ERP-MES-WMS Assistant`;
2. upload generated knowledge records;
3. use tags or folder names to separate ERP, MES, WMS, QC, and finance knowledge;
4. ask the assistant to cite the scenario and source type when answering.

## 4. Prompt suggestion

```text
You are a manufacturing digitalization assistant. Answer with practical steps.
When the question involves ERP, MES, WMS, APS, BOM, MRP, orders, inventory, work orders, quality inspection, delivery, or finance analysis, first identify the business scenario, then provide process steps, required fields, exception handling, and final output.
If information is missing, list the missing fields before giving a recommendation.
```
