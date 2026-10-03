from flask import Flask, request

app = Flask(__name__)
valor = "01101101"  # o que o jogo vai ler

@app.get("/dados")
def ler():
    return valor

@app.post("/dados")
def gravar():
    global valor
    valor = request.get_data(as_text=True)
    return "ok"

app.run(port=3000)
