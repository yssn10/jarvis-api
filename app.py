from flask import Flask, request, jsonify
import requests
import os

OPENROUTER_API_KEY = "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"

app = Flask(__name__)

@app.route("/")
def home():
    return "Jarvis is online"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_message = data.get("message", "")

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "Tu es Jarvis, un assistant intelligent, clair et utile."},
                {"role": "user", "content": user_message}
            ]
        }
    )

    try:
        answer = response.json()["choices"][0]["message"]["content"]
    except:
        answer = "Erreur IA"

    return jsonify({"response": answer})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
