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
                {"role": "user", "content": user_message}
            ]
        }
    )

    return jsonify({
        "status_code": response.status_code,
        "text": response.text
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
