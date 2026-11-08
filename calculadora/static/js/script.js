document.getElementById("btnLimpar").addEventListener("click", function () {

    // Limpa os campos do formulário
    document.getElementById("num1").value = "";
    document.getElementById("num2").value = "";

    // Remove o resultado da tela
    const resultado = document.getElementById("resultado");

    if (resultado) {
        resultado.remove();
    }

    // Retorna à página inicial
    window.location.href = "/";

});