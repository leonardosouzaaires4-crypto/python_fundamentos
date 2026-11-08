from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calcular", methods=["POST"])
def calcular():
    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    opcao = request.form["operacao"]

    if opcao == "soma":
        resultado = num1 + num2
    elif opcao == "subtracao":
        resultado = num1 - num2
    elif opcao == "multiplicacao":
        resultado = num1 * num2
    elif opcao == "divisao":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Não é possível dividir por zero."
    else:
        resultado = "Operação inválida!"

    if isinstance(resultado, (int, float)):
        resultado = f"{resultado:.2f}"

    return render_template(
        "index.html",
        resultado=resultado,
        num1=request.form["num1"],
        num2=request.form["num2"],
        operacao=opcao
    )


if __name__ == "__main__":
    app.run(debug=True)