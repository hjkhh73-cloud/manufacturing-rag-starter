# Manufacturing RAG Starter

**Manufacturing RAG Starter** is an open-source starter kit for building a small, practical manufacturing knowledge base that can be imported into RAG tools such as Dify, AnythingLLM, Open WebUI, or a custom FastAPI service.

The project focuses on common manufacturing digitalization scenarios:

- ERP / MES / WMS / APS business knowledge
- BOM, MRP, sales order, inventory, work order, quality inspection, delivery, and finance analysis
- SOP and implementation document preparation
- RAG-friendly Markdown / JSONL datasets for AI assistants

> Goal: help small and medium manufacturing teams turn scattered process notes into structured AI-ready knowledge assets.

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
- Dify / AnythingLLM import guidance
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

## Repository structure

```text
manufacturing-rag-starter/
├── data/                         # sample source knowledge
├── docs/                         # implementation and import guides
├── examples/                     # generated examples and prompts
├── src/mfg_rag_starter/          # Python CLI source code
├── .github/                      # issue templates and CI
├── pyproject.toml
├── LICENSE
└── README.md
```

## Roadmap

- [x] Basic CSV-to-JSONL knowledge builder
- [x] Manufacturing scenario taxonomy
- [x] Dify and AnythingLLM import guide
- [ ] Markdown folder ingestion
- [ ] SQLite metadata index
- [ ] FastAPI search demo
- [ ] More manufacturing templates: BOM, MRP, QC, delivery, finance analysis
- [ ] Evaluation question set for manufacturing RAG assistants

## Who may benefit

- manufacturing IT consultants;
- ERP / MES / WMS implementation teams;
- AI engineers building domain-specific RAG assistants;
- small factories starting their first AI knowledge base project;
- open-source contributors interested in industrial AI workflows.

## Contributing

Contributions are welcome. You can help by:

- adding manufacturing process templates;
- improving Dify / AnythingLLM import examples;
- adding evaluation questions;
- translating documentation;
- improving the CLI.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

MIT License. See [LICENSE](LICENSE).
