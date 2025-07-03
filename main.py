from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def chat():
    data = request.get_json()
    text = data.get("text", "")

    # Simulação da resposta (exemplo básico)
    if text.strip() == "":
        reply = "Não entendi. Pode repetir?"
    else:
        reply = f"Você disse: {text}"

    return jsonify(reply=reply)

@app.route("/", methods=["GET"])
def index():
    return "API ativa. Use POST para enviar mensagens."

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

