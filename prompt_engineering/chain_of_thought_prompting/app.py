from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:0.6b"


def ask_model(prompt, model_name=MODEL):
    data = {"model": model_name, "prompt": prompt, "stream": False}
    response = requests.post(OLLAMA_URL, json=data)
    return response.json()["response"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/solve", methods=["POST"])
def solve():
    question = request.json["question"]

    cot_prompt = f"""Solve this problem step by step, showing your reasoning clearly before giving the final answer.

Question: {question}

Let's think step by step:"""

    result = ask_model(cot_prompt)
    return jsonify({"reply": result})


if __name__ == "__main__":
    app.run(debug=True, port=5000)