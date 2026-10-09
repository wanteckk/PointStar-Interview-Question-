# PointStar Agentic Architect Challenge

## Project Overview

This repository contains my submission for the PointStar Agentic Architect Challenge. It covers three tasks involving system design, web scraping and AI agent development.

## Project Structure

| Part | Description |
|---|---|
| Part 1 — System Design | Agentic customer support email processing system |
| Part 2 — Technical Implementation | Web scraping and summarisation improvements |
| Part 3 — Practical Evaluation | Knowledge-based AI agent with conversation memory and a calculator tool |

Each part includes its own README with detailed setup instructions, implementation details and usage information where applicable.

## Requirements

- Python 3
- [Ollama](https://ollama.com/)
- Qwen3 4B model (`qwen3:4b`)

No external LLM API key is required. Parts 2 and 3 use a local Ollama model.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Replace the repository URL with your actual GitHub repository URL.

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

Follow the installation instructions in the README of the relevant part. Dependencies may differ between tasks.

### 4. Set Up Ollama

Install Ollama if necessary, then download the model:

```bash
ollama pull qwen3:4b
```

Make sure Ollama is running before executing the relevant Python scripts.

## Task Documentation

- **Part 1:** See the system design documents and architecture diagram.
- **Part 2:** See `Part2_Technical_Implementation/README.md`.
- **Part 3:** See `Part3_Practical_Evaluation/README.md`.

## Notes

- An internet connection is required for Part 2 to retrieve webpages.
- Part 3 uses the local knowledge base provided in its task folder.
- Run commands from the appropriate project directory, as described in each task's README.
- The project includes separate implementations and documentation for each task.

