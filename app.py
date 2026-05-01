from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Jarvis is online"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    response = f"Tu as dit : {user_message}"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()
