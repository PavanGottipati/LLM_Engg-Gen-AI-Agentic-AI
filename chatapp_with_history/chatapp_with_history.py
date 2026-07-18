from flask import Flask, request, jsonify
import requests, json

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:0.6b"

# Plain global list to store conversation history
history = [{"role": "system", "content": "You are a helpful assistant."}]


def call_ollama(messages):
    response = requests.post(OLLAMA_URL, json={"model": MODEL, "messages": messages, "stream": True}, stream=True)
    full_response = ""
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line)
            full_response += chunk.get("message", {}).get("content", "")
    return full_response


@app.route("/")
def home():
    return HTML_PAGE


@app.route("/chat", methods=["POST"])
def chat():
    global history
    prompt = request.json["prompt"]

    history.append({"role": "user", "content": prompt})
    reply = call_ollama(history)
    history.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})


@app.route("/reset", methods=["POST"])
def reset():
    global history
    history = [{"role": "system", "content": "You are a helpful assistant."}]
    return jsonify({"status": "cleared"})


HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Chat - With History</title>
</head>
<body style="font-family: 'Segoe UI', Arial, sans-serif; max-width: 600px; margin: 40px auto; background: #f0f2f5;">

  <div style="background: linear-gradient(135deg, #6a5af9, #d66efd); color: white; padding: 16px 20px; border-radius: 12px 12px 0 0; font-size: 18px; font-weight: 600; display: flex; justify-content: space-between; align-items: center;">
    <span>🧠 Chat (With History)</span>
    <button onclick="resetChat()"
      style="padding: 6px 14px; background: rgba(255,255,255,0.25); color: white; border: 1px solid white; border-radius: 14px; cursor: pointer; font-size: 12px;">
      Reset
    </button>
  </div>

  <div id="chat" style="background: white; border: 1px solid #ddd; border-top: none; padding: 15px; height: 380px; overflow-y: auto; display: flex; flex-direction: column;"></div>

  <div style="display: flex; gap: 8px; background: white; border: 1px solid #ddd; border-top: none; padding: 12px; border-radius: 0 0 12px 12px;">
    <input id="prompt" placeholder="Type a message..." onkeydown="if(event.key==='Enter') send()"
      style="flex: 1; padding: 10px 14px; border: 1px solid #ccc; border-radius: 20px; outline: none; font-size: 14px; box-sizing: border-box;">
    <button onclick="send()"
      style="padding: 10px 20px; background: #6a5af9; color: white; border: none; border-radius: 20px; cursor: pointer; font-size: 14px;">
      Send
    </button>
  </div>

  <script>
    async function send() {
      const promptBox = document.getElementById("prompt");
      const prompt = promptBox.value;
      if (!prompt) return;
      const chat = document.getElementById("chat");

      chat.innerHTML += `<div style="max-width:75%; padding:10px 14px; margin:6px 0; border-radius:16px; line-height:1.4; word-wrap:break-word; align-self:flex-end; background:#6a5af9; color:white; border-bottom-right-radius:4px;">${prompt}</div>`;
      promptBox.value = "";
      chat.scrollTop = chat.scrollHeight;

      const typingId = "typing-" + Date.now();
      chat.innerHTML += `<div id="${typingId}" style="align-self:flex-start; color:#999; font-style:italic; padding:10px 14px;">Bot is typing...</div>`;
      chat.scrollTop = chat.scrollHeight;

      const res = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({prompt})
      });
      const data = await res.json();

      document.getElementById(typingId).remove();
      chat.innerHTML += `<div style="max-width:75%; padding:10px 14px; margin:6px 0; border-radius:16px; line-height:1.4; word-wrap:break-word; align-self:flex-start; background:#e9e9eb; color:#222; border-bottom-left-radius:4px;">${data.reply}</div>`;
      chat.scrollTop = chat.scrollHeight;
    }

    async function resetChat() {
      await fetch("/reset", {method: "POST"});
      document.getElementById("chat").innerHTML = "";
    }
  </script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True, port=5001)