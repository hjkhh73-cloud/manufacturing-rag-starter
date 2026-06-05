# Manufacturing RAG Starter

[![CI](https://github.com/hjkhh73-cloud/manufacturing-rag-starter/actions/workflows/ci.yml/badge.svg)](https://github.com/hjkhh73-cloud/manufacturing-rag-starter/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)

**Manufacturing RAG Starter** is an open-source starter kit for building practical manufacturing knowledge bases that can be imported into RAG tools such as Dify, AnythingLLM, Open WebUI, or a custom FastAPI service.

The project focuses on manufacturing digitalization scenarios where business context matters as much as code:

- ERP / MES / WMS / APS business knowledge
- BOM, MRP, sales orders, inventory, work orders, quality inspection, delivery, and finance analysis
- SOP and implementation document preparation
- RAG-friendly Markdown / JSONL datasets for AI assistants

> Goal: help small and medium manufacturing teams turn scattered process notes into structured AI-ready knowledge assets.

## Project status

This repository is an early-stage but working starter kit.

Current capabilities:

- CSV to JSONL knowledge conversion
- manufacturing sample records
- Dify / AnythingLLM import guide
- scenario taxonomy
- unit tests
- GitHub Actions CI

Planned next steps are tracked in [ROADMAP.md](ROADMAP.md).

## Why this project exists

Many manufacturing AI projects fail before the model is selected because the source knowledge is messy: process notes are scattered across documents, spreadsheets, chats, and personal notes. This starter kit provides a simple and transparent workflow:

1. collect manufacturing process knowledge;
2. normalize it into Markdown or CSV;
3. generate RAG-friendly JSONL chunks;
4. import the result into Dify, AnythingLLM, or another knowledge base;
5. test the assistant with real ERP/MES/WMS questions.

## Features

- Minimal Python CLI with no required third-party runtime dependencies
- Manufacturing scenario templates
- Sample ERP/MES/WMS knowledge records
- JSONL chunk output for downstream RAG systems
- Reusable manufacturing evaluation questions and retrieval baseline
- Dify / AnythingLLM import guidance
- English and Chinese documentation
- Open-source documentation suitable for continuous community improvement

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m mfg_rag_starter build --input data/sample_knowledge.csv --output examples/manufacturing_kb.jsonl
```

Preview generated JSONL:

```bash
python -m mfg_rag_starter preview --input examples/manufacturing_kb.jsonl --limit 3
```

Chinese quick start: [docs/zh-cn/快速开始.md](docs/zh-cn/快速开始.md)

## Example output

Each generated JSONL record includes both readable text and structured metadata:

```json
{
  "id": "KB-ERP-001",
  "title": "Sales order to production order",
  "scenario": "ERP/MES integration",
  "source_type": "SOP",
  "tags": ["ERP", "MES", "sales order", "production order"],
  "text": "# Sales order to production order...",
  "metadata": {
    "id": "KB-ERP-001",
    "scenario": "ERP/MES integration"
  }
}
```

## Example use cases

### 1. ERP/MES implementation assistant

Use the generated knowledge base to answer questions such as:

- What is the difference between a sales order, production order, and work order?
- How should an ERP-MES integration handle BOM version changes?
- What exception handling is needed when WMS inventory is inconsistent with MES consumption?

### 2. Manufacturing SOP assistant

Convert SOP notes into RAG chunks so that an AI assistant can help frontline users understand:

- how to create a work order;
- how to handle quality inspection exceptions;
- how to record material picking and production reporting;
- how to escalate delivery risks.

### 3. Dify / AnythingLLM knowledge base starter

Use `examples/manufacturing_kb.jsonl` as a clean, structured source for a knowledge base. Each record contains title, scenario, source type, tags, and content.

Import guide: [docs/dify-anythingllm-import-guide.md](docs/dify-anythingllm-import-guide.md)

Run the manufacturing retrieval baseline:

```bash
python -m mfg_rag_starter evaluate \
  --knowledge examples/manufacturing_kb.jsonl \
  --questions evaluation/manufacturing_eval_questions.jsonl \
  --output evaluation/baseline_results.json \
  --top-k 1
```

## Documentation

- [Architecture](docs/architecture.md)
- [Evaluation guide](docs/evaluation-guide.md)
- [Project impact](docs/project-impact.md)
- [Scenario taxonomy](docs/scenario-taxonomy.md)
- [Dify / AnythingLLM import guide](docs/dify-anythingllm-import-guide.md)
- [Chinese quick start](docs/zh-cn/快速开始.md)
- [Roadmap](ROADMAP.md)

## Repository structure

```text
manufacturing-rag-starter/
├── data/                         # sample source knowledge
├── docs/                         # implementation and import guides
├── evaluation/                   # evaluation questions and baseline results
├── examples/                     # generated examples and prompts
├── src/mfg_rag_starter/          # Python CLI source code
├── tests/                        # unit tests
├── .github/                      # issue templates and CI
├── pyproject.toml
├── ROADMAP.md
├── LICENSE
└── README.md
```

## Who may benefit

- manufacturing IT consultants;
- ERP / MES / WMS implementation teams;
- AI engineers building domain-specific RAG assistants;
- small factories starting their first AI knowledge base project;
- open-source contributors interested in industrial AI workflows.

## Development

Run tests:

```bash
python -m unittest discover -s tests
```

Regenerate the sample JSONL file:

```bash
python -m mfg_rag_starter build --input data/sample_knowledge.csv --output examples/manufacturing_kb.jsonl
```

Run the retrieval baseline:

```bash
python -m mfg_rag_starter evaluate --knowledge examples/manufacturing_kb.jsonl --questions evaluation/manufacturing_eval_questions.jsonl --output evaluation/baseline_results.json --top-k 1
```

## Contributing

Contributions are welcome. You can help by:

- adding manufacturing process templates;
- improving Dify / AnythingLLM import examples;
- adding evaluation questions;
- translating documentation;
- improving the CLI.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Security and privacy

Do not commit customer-sensitive information, private contracts, production data, employee personal data, credentials, or proprietary implementation documents. Use synthetic or anonymized examples when contributing.

See [SECURITY.md](SECURITY.md) for responsible disclosure guidance.

## License

MIT License. See [LICENSE](LICENSE).
