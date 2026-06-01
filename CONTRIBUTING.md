# Contributing

Thank you for considering a contribution to Manufacturing RAG Starter.

## Good first contributions

- Add manufacturing process templates.
- Improve ERP / MES / WMS scenario examples.
- Add Dify or AnythingLLM import notes.
- Add evaluation questions for manufacturing RAG assistants.
- Improve English or Chinese documentation.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m mfg_rag_starter build --input data/sample_knowledge.csv --output examples/manufacturing_kb.jsonl
```

## Pull request checklist

- Keep examples realistic and non-sensitive.
- Do not include customer confidential data.
- Prefer clear business language over heavy technical jargon.
- Add or update documentation when changing behavior.
