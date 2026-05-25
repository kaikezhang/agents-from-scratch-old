# Quick Start Guide

Get up and running with AI Agents from Scratch in 5 minutes.

This repo now talks to the **DeepSeek API** (an OpenAI-compatible endpoint).
DeepSeek is used because it is extremely cheap — running all 12 lessons end-to-end
typically costs well under $0.10. See [pricing](https://api-docs.deepseek.com/quick_start/pricing).

## Prerequisites

- Python 3.10 or higher
- A DeepSeek API key (free signup, then top up a small amount of credit)

## Step 1: Install Dependencies

```bash
# (Optional) create a virtual environment first
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Step 2: Get a DeepSeek API Key

1. Sign up at https://platform.deepseek.com/
2. Create an API key in the dashboard
3. Export it in your shell:

```bash
export DEEPSEEK_API_KEY=sk-...
```

Add the line to your `~/.zshrc` / `~/.bashrc` if you want it to persist.

### Using a different OpenAI-compatible endpoint

The `LLM` class also reads these env vars, so you can point it elsewhere
without touching code:

- `DEEPSEEK_BASE_URL` or `OPENAI_BASE_URL` — defaults to `https://api.deepseek.com`
- `OPENAI_API_KEY` — used as a fallback if `DEEPSEEK_API_KEY` is not set
- `LLM_MODEL` — defaults to `deepseek-chat`

Examples:
- Official OpenAI: `OPENAI_BASE_URL=https://api.openai.com/v1` + `OPENAI_API_KEY=...` + `LLM_MODEL=gpt-4o-mini`
- Local Ollama: `OPENAI_BASE_URL=http://localhost:11434/v1` + `OPENAI_API_KEY=ollama` + `LLM_MODEL=llama3.1`

## Step 3: Verify Setup

```bash
python setup_check.py
```

This checks Python version, the `openai` package, your API key, and the
repository structure.

## Step 4: Run Examples

```bash
python complete_example.py
```

This runs all 12 lessons against DeepSeek. Open the file to comment out
lessons you want to skip.

## Step 5: Start Learning

Now read the lessons in order:

1. `lessons/01_basic_llm_chat.md` — Understanding the basics
2. `lessons/02_system_prompt.md` — Adding behavior
3. `lessons/03_structured_output.md` — Making it reliable
4. … and so on through lesson 12

Each lesson builds on the previous one.

## Troubleshooting

### `RuntimeError: No API key found`

You haven't set `DEEPSEEK_API_KEY`. Run `export DEEPSEEK_API_KEY=sk-...` in
the same shell before launching the script.

### `openai.AuthenticationError` / 401

Your key is wrong or has no credit. Check the DeepSeek dashboard.

### Rate limits / slow responses

DeepSeek occasionally throttles. Re-run, or lower concurrency. Each call
takes ~1–3 seconds, much faster than local CPU inference used to be.

## Tips for Success

1. **Don't skip lessons** — they build on each other
2. **Run the code** — reading isn't enough
3. **Experiment** — modify examples and see what happens
4. **Read comments** — the code explains the "why"

Happy learning! 🚀
