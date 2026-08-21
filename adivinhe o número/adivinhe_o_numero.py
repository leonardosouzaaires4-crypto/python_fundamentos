import random

def jogar():
    num_secreto = random.randint(1, 100)
    num_tentativas = 0

    print("\nJOGO DE ADIVINHAÇÃO")

    num = int(input("Digite um número entre 1 e 100 ou 0 para desistir: "))

    while num < 0 or num > 100:
        print("Número inválido. Digite um número entre 1 e 100 ou 0 para desistir.")
        num = int(input("Digite um número entre 1 e 100 ou 0 para desistir: "))

    while num != num_secreto:

        if num == 0:
            print("Você desistiu, mas o número secreto era:", num_secreto)
            return

        num_tentativas += 1

        if num < num_secreto:
            print("O número secreto é maior.")
        else:
            print("O número secreto é menor.")

        num = int(input("Tente novamente: "))

    num_tentativas += 1

    print(f"Parabéns! Você acertou o número secreto com {num_tentativas} tentativas.")


# Inicia o primeiro jogo
jogar()

# Pergunta se deseja jogar novamente
while True:

    jogar_novamente = input("\nDeseja jogar novamente? ").lower()

    if jogar_novamente == "s" or jogar_novamente == "sim":
        jogar()

    elif jogar_novamente == "n" or jogar_novamente == "não":
        print("Obrigado por jogar!")
        break

    else:
        print("Opção inválida. Digite sim ou não.")