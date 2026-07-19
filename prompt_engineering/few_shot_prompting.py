from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:0.6b"


def ask_model(prompt, model_name=MODEL):
    """Send a prompt to Ollama and return the response text."""
    data = {
        "model": model_name,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=data)
    return response.json()["response"]


def clean_response(text):
    """Remove <think>...</think> reasoning blocks if the model includes them."""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return text.strip()


def extract_label(text):
    """Grab just the last non-empty line, in case the model still rambles."""
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
    return lines[-1] if lines else text.strip()


@app.route("/")
def home():
    return HTML_PAGE


@app.route("/classify", methods=["POST"])
def classify():
    review = request.json["review"]

    few_shot_prompt = f"""/no_think
Classify each review as exactly one of: positive, negative, or mixed. Reply with ONLY the single label word, no explanation.
Review: 'Absolutely loved it, will buy again!'
Classification: positive
Review: 'Broke after two days, waste of money'
Classification: negative
Review: 'Great camera quality but battery dies fast'
Classification: mixed
Review: '{review}'
Classification:"""

    result = ask_model(few_shot_prompt)
    result = clean_response(result)
    result = extract_label(result)

    return jsonify({"reply": result})


HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Few-Shot Review Classifier</title>
</head>
<body style="font-family: 'Segoe UI', Arial, sans-serif; max-width: 600px; margin: 40px auto; background: #f0f2f5;">

  <div style="background: linear-gradient(135deg, #6a5af9, #d66efd); color: white; padding: 16px 20px; border-radius: 12px 12px 0 0; font-size: 18px; font-weight: 600;">
    🏷️ Few-Shot Review Classifier
  </div>

  <div style="background: white; border: 1px solid #ddd; border-top: none; padding: 20px; border-radius: 0 0 12px 12px;">
    <p style="color:#555; font-size:14px; margin-top:0;">
      Enter a customer review. The model is given <b>3 labeled examples</b> (positive, negative, mixed) before classifying yours — few-shot prompting.
    </p>

    <textarea id="review" rows="4" placeholder="e.g. The food was amazing but the service was terrible and we waited 45 minutes"
      style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 8px; font-size: 14px; box-sizing: border-box; resize: vertical;"></textarea>

    <button onclick="classify()"
      style="margin-top: 10px; padding: 10px 20px; background: #6a5af9; color: white; border: none; border-radius: 20px; cursor: pointer; font-size: 14px;">
      Classify
    </button>

    <div id="result" style="margin-top: 20px; padding: 14px; background: #e9e9eb; border-radius: 10px; display: none; white-space: pre-wrap; color:#222;"></div>
  </div>

  <script>
    async function classify() {
      const review = document.getElementById("review").value;
      if (!review) return;

      const resultBox = document.getElementById("result");
      resultBox.style.display = "block";
      resultBox.innerText = "Classifying...";

      const res = await fetch("/classify", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({review})
      });
      const data = await res.json();

      resultBox.innerText = data.reply;
    }
  </script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True, port=5001)