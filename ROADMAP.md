# Roadmap

This roadmap describes the planned direction for Manufacturing RAG Starter. It is intentionally practical and focused on small, verifiable improvements.

## 0. Current status

Completed:

- CSV to JSONL knowledge builder
- Manufacturing sample knowledge records
- Dify / AnythingLLM import guidance
- Upload-ready Markdown export and reproducible import example
- Scenario taxonomy for ERP, MES, WMS, APS, BOM, MRP, quality, delivery, and finance analysis
- Manufacturing evaluation question set and retrieval baseline
- Basic unit tests and GitHub Actions CI

## 1. Short-term improvements

### 1.1 Markdown folder ingestion

Goal: allow users to convert a folder of Markdown SOPs into JSONL chunks.

Expected work:

- read `.md` files recursively;
- preserve document path as metadata;
- split content by headings;
- output RAG-ready JSONL records.

Why it matters:

Many manufacturing implementation notes are already stored in Markdown, Obsidian, or exported documentation. Folder ingestion will reduce manual CSV preparation.

### 1.2 More domain templates

Goal: add reusable templates for common manufacturing knowledge assets.

Planned templates:

- BOM version change explanation;
- MRP shortage analysis;
- MES work order execution;
- WMS picking and material return;
- quality inspection exception handling;
- delivery risk escalation;
- finance operation analysis.

## 2. Medium-term improvements

### 2.1 SQLite metadata index

Goal: add a small local metadata index for knowledge records.

Expected work:

- store record id, title, scenario, tags, source path, and timestamps;
- support simple search and filtering;
- avoid requiring an external database.

### 2.2 FastAPI search demo

Goal: provide a minimal backend service for searching and previewing knowledge records.

Expected work:

- `/health` endpoint;
- `/records` endpoint;
- `/search` endpoint;
- simple examples for local testing.

## 3. Long-term direction

The long-term goal is not to become a large enterprise platform. The goal is to remain a lightweight, understandable, open-source starter kit for manufacturing AI knowledge projects.

Potential future work:

- connectors for ERP/MES/WMS export files;
- multilingual documentation;
- retrieval evaluation examples;
- optional OpenAI / local model prompt evaluation scripts;
- manufacturing-specific agent workflow examples.

## Contribution priorities

Good first contributions:

- add one manufacturing scenario template;
- improve a sample question;
- translate a document;
- add a small test case;
- improve Dify or AnythingLLM setup notes.

Please keep contributions practical, transparent, and easy for manufacturing teams to understand.
