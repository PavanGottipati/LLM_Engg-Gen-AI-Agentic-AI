# Naive Product Information Extraction

This project demonstrates a basic approach to extracting product information from customer reviews using a Large Language Model.

## Problem

Given a review:

"I bought the wireless earbuds for 2500 rupees. Sound quality is great, battery lasts 6 hours, but the charging case feels cheap."

We ask the LLM:

```text
Extract the product details from this review.
```

## Example Output

```text
Product: Wireless Earbuds
Price: 2500 Rupees
Pros:
- Great sound quality
- Battery lasts 6 hours

Cons:
- Charging case feels cheap
```

## Limitation

The output format may change between requests.

Examples:

Request 1:

```text
Product: Wireless Earbuds
Price: 2500
```

Request 2:

```text
The customer purchased wireless earbuds for ₹2500.
```

This makes automation difficult.

## Tech Stack

- Python
- Flask
- Ollama
- Qwen

## Run

```bash
pip install -r requirements.txt
python app.py
```