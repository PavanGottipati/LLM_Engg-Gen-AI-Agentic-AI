# Structured Outputs with Pydantic Validation

This project demonstrates how to generate reliable structured data from an LLM using:

- Structured Prompting
- JSON Output
- Pydantic Validation

## Problem

Given a review:

```text
I bought the wireless earbuds for 2500 rupees.
Sound quality is great.
Battery lasts 6 hours.
Charging case feels cheap.
```

We force the model to return:

```json
{
  "product_name": "wireless earbuds",
  "price": 2500,
  "currency": "rupees",
  "pros": [
    "great sound quality",
    "battery lasts 6 hours"
  ],
  "cons": [
    "charging case feels cheap"
  ],
  "overall_sentiment": "mixed"
}
```

## Why Structured Outputs?

### Naive Extraction

❌ Inconsistent format

❌ Hard to parse

❌ Not production ready

### Structured Outputs

✅ Consistent JSON

✅ API friendly

✅ Database ready

✅ Easy validation

## Architecture

```text
Review
 ↓
Structured Prompt
 ↓
Qwen
 ↓
JSON Output
 ↓
JSON Parsing
 ↓
Pydantic Validation
 ↓
Application
```

## Tech Stack

- Python
- Flask
- Ollama
- Qwen
- Pydantic

## Run

```bash
pip install -r requirements.txt
python app.py
```