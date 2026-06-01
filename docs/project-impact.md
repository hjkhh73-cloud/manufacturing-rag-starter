# Project Impact

Manufacturing RAG Starter exists to help manufacturing teams and AI builders move from scattered process notes to testable AI knowledge bases.

## Problem

Many manufacturing AI assistant projects do not fail because the model is weak. They fail because the source knowledge is not prepared:

- SOPs are scattered across Word files, spreadsheets, chats, and personal notes;
- ERP, MES, WMS, APS, BOM, and MRP concepts are mixed without clear boundaries;
- implementation knowledge is often stored in consultants' experience rather than reusable templates;
- knowledge-base imports are hard to test consistently;
- business teams cannot easily see the difference between a demo chatbot and a reliable workflow assistant.

## What this project provides

This project provides a lightweight path:

1. define manufacturing scenarios;
2. normalize process knowledge into simple records;
3. generate portable JSONL data;
4. import into Dify, AnythingLLM, or a custom RAG service;
5. test with real manufacturing questions.

## Target users

- Manufacturing IT consultants
- ERP / MES / WMS implementation teams
- AI engineers building domain-specific RAG assistants
- Small and medium factories exploring practical AI tools
- Open-source contributors interested in industrial AI workflows

## Example business outcomes

With a prepared knowledge base, teams can build assistants that help answer questions such as:

- How should a sales order become a production order?
- What should happen when BOM versions change after a work order is released?
- How should WMS and MES handle inventory mismatch?
- How should quality inspection exceptions be escalated?
- What finance and delivery indicators should managers review weekly?

## Why open source matters

Manufacturing digitalization knowledge is often locked inside projects, vendors, and private documents. An open starter kit makes it easier to share reusable structures without exposing customer-sensitive data.

The project is intentionally small so that new contributors can understand it, improve it, and adapt it to their own local manufacturing scenarios.

## How Codex can help

Codex can help maintain and grow this project by:

- improving documentation quality;
- generating tests for CLI behavior;
- reviewing planned FastAPI and SQLite code;
- helping turn manufacturing scenarios into reusable templates;
- assisting with issue triage and contributor onboarding;
- improving examples for Dify, AnythingLLM, and custom RAG workflows.
