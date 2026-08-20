# Calculadora em Python

Projeto desenvolvido em **Python** como parte dos estudos de fundamentos da linguagem.

A aplicação funciona diretamente pelo terminal e permite ao usuário realizar operações matemáticas básicas por meio de um menu interativo.

## Objetivo

Praticar conceitos fundamentais de programação utilizando Python, como:

* Estruturas de repetição;
* Estruturas condicionais;
* Entrada de dados pelo usuário;
* Conversão de tipos;
* Operadores matemáticos;
* Interpolação de strings;
* Controle do fluxo de execução.

## Funcionalidades

A calculadora possui as seguintes operações:

| Opção | Operação             |
| ----- | -------------------- |
| 1     |  Soma                |
| 2     |  Subtração           |
| 3     |  Multiplicação       |
| 4     |  Divisão             |
| 5     |  Encerrar o programa |

Além disso, o programa possui algumas validações:

* Impede a divisão por zero;
* Informa quando uma opção inválida é selecionada;
* Permite realizar várias operações sem precisar reiniciar o programa.

## Tecnologias

*  Python
*  Terminal / Console

## Como executar

Certifique-se de ter o Python instalado.

No terminal, navegue até a pasta do projeto:

cd calculadora

Execute o programa:

python calculadora.py

Em alguns ambientes, pode ser necessário utilizar:

python3 calculadora.py

## Exemplo de execução

===== CALCULADORA =====
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair

Escolha uma opção: 1
Digite o primeiro número: 10
Digite o segundo número: 5

Resultado: 15.0

### Divisão por zero

O programa também possui uma verificação para evitar uma divisão inválida:

Escolha uma opção: 4
Digite o primeiro número: 10
Digite o segundo número: 0

Não é possível dividir por zero.

### Opção inválida

Caso o usuário escolha uma opção que não esteja disponível:

Escolha uma opção: 8

Opção inválida!

## Conceitos praticados

Este projeto utiliza principalmente:

### `while`

Mantém a calculadora funcionando até que o usuário escolha a opção de saída.

while True:

### `if / elif / else`

Utilizados para identificar a operação escolhida e controlar diferentes situações.

### `input()`

Permite receber informações digitadas pelo usuário.

### `float()`

Converte os números informados pelo usuário para valores que podem possuir casas decimais.

### `break`

Encerra o loop quando o usuário escolhe a opção `5`.

### f-strings

Utilizadas para apresentar os resultados das operações:

print(f"Resultado: {num1 + num2}")

## Possíveis melhorias futuras

Como parte da evolução do projeto, algumas funcionalidades podem ser adicionadas posteriormente:

* Criar funções separadas para cada operação;
* Adicionar tratamento para entradas que não sejam números;
* Permitir operações com mais de dois números;
* Criar histórico de operações;
* Melhorar a organização do código;
* Criar uma interface gráfica.

## Status

**Concluído — versão inicial**

O projeto poderá receber novas funcionalidades conforme novos conceitos de Python forem estudados.

---

Projeto desenvolvido durante meus estudos de **Python e lógica de programação**.
