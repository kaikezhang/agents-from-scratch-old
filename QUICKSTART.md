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

1. Sign up at https://platform.deepseek.com/ and create an API key.
2. Copy the example env file and paste your key in:

```bash
cp .env.example .env
# then edit .env and set DEEPSEEK_API_KEY=sk-...
```

`.env` is gitignored, so your key stays local. The repo loads it
automatically — no need to `export` anything in your shell.

> Prefer shell exports? They still work and take precedence over `.env`.

### Using a different OpenAI-compatible endpoint

The same `.env` file can point the LLM wrapper at any OpenAI-compatible
endpoint. See `.env.example` for ready-to-use blocks for **OpenAI** and
**local Ollama**. The relevant variables:

- `DEEPSEEK_BASE_URL` or `OPENAI_BASE_URL` — defaults to `https://api.deepseek.com`
- `OPENAI_API_KEY` — fallback if `DEEPSEEK_API_KEY` is not set
- `LLM_MODEL` — defaults to `deepseek-chat`

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

`DEEPSEEK_API_KEY` isn't set. Either:
- create a `.env` (copy from `.env.example`) and put your key there, or
- `export DEEPSEEK_API_KEY=sk-...` in the same shell before launching the script.

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
