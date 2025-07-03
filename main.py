from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "API rodando!"

@app.route("/mensagem", methods=["POST"])
def mensagem():
    data = request.json
    texto = data.get("texto", "")
    resposta = f"Você disse: {texto}"
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
