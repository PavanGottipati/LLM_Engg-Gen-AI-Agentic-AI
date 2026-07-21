from flask import Flask, request, jsonify, render_template
from pydantic import BaseModel
from typing import List
import requests
import json

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:0.6b"


class ProductReview(BaseModel):
    product_name: str
    price: float
    currency: str
    pros: List[str]
    cons: List[str]
    overall_sentiment: str


def ask_model(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/extract", methods=["POST"])
def extract():

    review = request.json["review"]

    prompt = f"""
Extract product information from the review.

Return ONLY valid JSON.

{{
  "product_name":"string",
  "price":0,
  "currency":"string",
  "pros":[""],
  "cons":[""],
  "overall_sentiment":"positive, negative, or mixed"
}}

Review:
{review}
"""

    response = ask_model(prompt)

    start = response.find("{")
    end = response.rfind("}") + 1

    parsed = json.loads(response[start:end])

    validated = ProductReview(**parsed)

    return jsonify(validated.model_dump())


if __name__ == "__main__":
    app.run(debug=True, port=5001)