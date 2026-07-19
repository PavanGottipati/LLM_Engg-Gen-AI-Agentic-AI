from flask import Flask, request, jsonify
import requests

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


@app.route("/")
def home():
    return HTML_PAGE


@app.route("/classify", methods=["POST"])
def classify():
    review = request.json["review"]

    zero_shot_prompt = f"Classify this review as positive, negative, or mixed: '{review}'"
    result = ask_model(zero_shot_prompt)

    return jsonify({"reply": result})


HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Zero-Shot Review Classifier</title>
</head>
<body style="font-family: 'Segoe UI', Arial, sans-serif; max-width: 600px; margin: 40px auto; background: #f0f2f5;">

  <div style="background: linear-gradient(135deg, #6a5af9, #d66efd); color: white; padding: 16px 20px; border-radius: 12px 12px 0 0; font-size: 18px; font-weight: 600;">
    🏷️ Zero-Shot Review Classifier
  </div>

  <div style="background: white; border: 1px solid #ddd; border-top: none; padding: 20px; border-radius: 0 0 12px 12px;">
    <p style="color:#555; font-size:14px; margin-top:0;">Enter a customer review. The model will classify it as <b>positive</b>, <b>negative</b>, or <b>mixed</b> — with no examples given (zero-shot).</p>

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
    app.run(debug=True, port=5000)