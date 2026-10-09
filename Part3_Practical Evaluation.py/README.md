# PointStar Part 3 — Practical Evaluation

A simple LangGraph agent using the local `qwen3:4b` model through Ollama. It answers from `knowledge.txt`, keeps conversation memory while the program is running, and can call a calculator tool.

## Requirements
- Python 3
- Ollama installed
- `qwen3:4b` model downloaded

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
ollama pull qwen3:4b
```
Make sure the Ollama app is running. If needed, start it in a separate terminal with `ollama serve`.

## Run
```bash
python main.py
```

## Calculator unit tests
```bash
python -m unittest test_agent.py -v
```

Logs are written to the terminal and `agent.log`. Conversation memory uses `MemorySaver`, so it is temporary and cleared when the program stops.
