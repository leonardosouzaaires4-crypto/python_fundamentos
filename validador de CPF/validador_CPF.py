cpf = input("Digite o CPF para validação: ")

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        print("CPF inválido. O CPF deve conter 11 dígitos.")
        return False

    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        print("CPF inválido. Todos os dígitos são iguais.")
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = (soma * 10 % 11) % 10

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = (soma * 10 % 11) % 10

    # Verifica se os dígitos verificadores estão corretos
    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"

if validar_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")