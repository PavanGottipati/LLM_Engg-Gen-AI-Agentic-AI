# 💬 LangChain Conversation Memory Chatbot

A simple AI chatbot built using **Flask**, **LangChain**, and **Ollama** that demonstrates **Conversation Memory**. The chatbot remembers previous interactions within the same session, enabling context-aware, multi-turn conversations.

## 🚀 Features

- 🤖 Chat with a locally running LLM using Ollama
- 🧠 Conversation Memory using LangChain
- 💬 Multi-turn conversations with context awareness
- 🔄 Clear chat history anytime
- 🌐 Flask-based web interface
- ⚡ Lightweight and easy to run locally

## 🛠️ Tech Stack

- Python
- Flask
- LangChain
- Ollama
- Qwen 3 (0.6B)
- HTML
- JavaScript

## 📂 Project Structure

```
chatbot/
│
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Download the model

```bash
ollama pull qwen3:0.6b
```

Run Ollama

```bash
ollama serve
```

Start the Flask application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 🧠 Conversation Memory

Unlike a stateless chatbot, this application stores previous conversations as:

- HumanMessage
- AIMessage

These messages are injected back into the prompt using a **Messages Placeholder**, allowing the LLM to answer follow-up questions with context.

Example:

```
User: My name is Pavan.

Bot: Nice to meet you, Pavan!

User: What's my name?

Bot: Your name is Pavan.
```

---

## 📸 Demo

<img src="demo.png" width="900">

---

## 📚 Concepts Demonstrated

- LangChain Prompt Templates
- ChatOllama
- StrOutputParser
- Conversation Memory
- HumanMessage
- AIMessage
- Stateful Chatbots
- Prompt Chaining

---

## 🔮 Future Improvements

- Streaming responses
- Chat history database
- User authentication
- Multiple LLM support
- RAG integration
- Vector Database

---

## ⭐ If you found this useful, consider giving the repository a star!