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

    tot_prompt = f"""Solve this problem using Tree-of-Thought reasoning:

Question: {question}

Step 1: Generate 3 different possible approaches (branches) to solve this.
Step 2: Briefly evaluate each approach's likelihood of being correct.
Step 3: Pick the best approach and give the final answer clearly.

Format your response as:
Approach 1: ...
Approach 2: ...
Approach 3: ...
Evaluation: ...
Final Answer: ..."""

    result = ask_model(tot_prompt)
    return jsonify({"reply": result})


if __name__ == "__main__":
    app.run(debug=True, port=5006)