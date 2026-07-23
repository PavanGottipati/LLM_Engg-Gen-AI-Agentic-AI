from flask import Flask, render_template, request, jsonify, session
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

app = Flask(__name__)
app.secret_key = "your-secret-key"

# Load Model
model = ChatOllama(model="qwen3:0.6b")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer briefly and clearly. /nothink",
        ),
        ("placeholder", "{history}"),
        ("human", "{question}"),
    ]
)

parser = StrOutputParser()

chain = prompt | model | parser


def get_history():
    """
    Convert session history into LangChain message objects.
    """
    history = []

    if "history" not in session:
        session["history"] = []

    for msg in session["history"]:
        if msg["role"] == "human":
            history.append(HumanMessage(content=msg["content"]))
        else:
            history.append(AIMessage(content=msg["content"]))

    return history


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json.get("message")

    history = get_history()

    response = chain.invoke(
        {
            "question": user_message,
            "history": history,
        }
    )

    session["history"].append(
        {
            "role": "human",
            "content": user_message,
        }
    )

    session["history"].append(
        {
            "role": "ai",
            "content": response,
        }
    )

    session.modified = True

    return jsonify(
        {
            "response": response,
        }
    )


@app.route("/clear")
def clear():
    session.pop("history", None)
    return jsonify({"message": "Memory Cleared"})


if __name__ == "__main__":
    app.run(debug=True)