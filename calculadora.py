while True:
    print("\n===== CALCULADORA =====")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Programa encerrado!")
        break

    if opcao in ["1", "2", "3", "4"]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            print(f"Resultado: {num1 + num2}")

        elif opcao == "2":
            print(f"Resultado: {num1 - num2}")

        elif opcao == "3":
            print(f"Resultado: {num1 * num2}")

        elif opcao == "4":
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Não é possível dividir por zero.")

    else:
        print("Opção inválida!")