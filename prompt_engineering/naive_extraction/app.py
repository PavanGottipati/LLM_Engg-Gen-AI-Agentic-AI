from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:0.6b"


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
Extract the product details from this review:

{review}
"""

    result = ask_model(prompt)

    return jsonify({
        "reply": result
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)