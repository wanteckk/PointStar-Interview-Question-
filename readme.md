# PointStar Agentic Architect Challenge

## Project Overview

This project contains three parts:

- **Part 1:** Design an agentic customer support email system.
- **Part 2:** Improve a web scraping and summarisation script.
- **Part 3:** Build a simple AI agent that answers questions using a knowledge base, remembers previous conversations and uses a calculator tool when needed.

## Requirements

- Python 
- Ollama
- Qwen3 4B model

No external LLM API key is required because the project uses a local Ollama model.

## Setup Instructions

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install requests beautifulsoup4 langchain-ollama langgraph
```

### 3. Install and start Ollama

Install Ollama from https://ollama.com if it is not already installed.

Download the model:

```bash
ollama pull qwen3:4b
```

Make sure Ollama is running before executing the Python scripts.

## How to Run

### Part 2 — Web Scraping and Summarisation

```bash
python Part 2 - Technical Implementation.py

The script extracts webpage content, splits long text into smaller chunks, summarises the content and limits the final summary to three bullet points.

### Part 3 — AI Agent

```bash
python Part 3 - Practical Evaluation.py
```

The agent answers questions using `knowledge.txt`, remembers previous messages within the same conversation thread and calls a calculator tool when needed.

## Part 1 — System Design

The architecture diagram and design brief are provided separately. The design includes critical issue escalation, email classification, knowledge base retrieval, response drafting and human review.

## Notes

- Ensure Ollama is running and the `qwen3:4b` model is available before running the scripts.
- An internet connection is required to scrape webpages in Part 2.
- The knowledge base for Part 3 is stored in `knowledge.txt`.
- The scripts should be run from the project root directory.