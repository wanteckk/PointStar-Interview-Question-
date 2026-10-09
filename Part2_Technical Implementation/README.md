# Part 2 — Web Scraping and Summarisation

This script downloads a webpage, removes common non-content HTML elements, extracts text, splits long pages into chunks, and uses the local Qwen3 4B model through Ollama to create a concise summary of up to three bullet points.

## Requirements

- Python 3
- Ollama installed and running
- `qwen3:4b` model downloaded

## Setup

Run these commands from the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install requests beautifulsoup4 langchain-ollama
ollama pull qwen3:4b
```

On macOS, you can open the Ollama app before running the script. If Ollama is not running as a service, start it in another terminal with `ollama serve`.

## Run

```bash
python Part2_Web_Scraper/main.py
```

Change `target_url` at the bottom of `main.py` to test another webpage.

## Tests

```bash
python -m unittest discover -s Part2_Web_Scraper -p "test_*.py" -v
```

The tests check text chunking, invalid chunk sizes, the three-bullet output limit, and empty model responses. They mock the LLM for unit tests, so the tests do not need to call the model.

## Logging and failure handling

The script logs the extracted text length, number of chunks, progress, errors, and total processing time to the terminal and `scraper.log`. HTTP timeouts, HTTP errors, empty page content and LLM failures are reported rather than silently ignored.

The final output is limited to three bullet points by a programmatic guardrail. This limits the format and length, but does not guarantee that every generated statement is factually correct.
