# Jogo de Adivinhação em Python

Projeto desenvolvido em **Python** como parte dos estudos de fundamentos da linguagem e lógica de programação.

O programa sorteia aleatoriamente um número entre **1 e 100**, e o jogador deve tentar descobrir qual é o número secreto. A cada tentativa, o programa informa se o número secreto é maior ou menor que o palpite.

## Funcionalidades

*  Geração aleatória de um número entre 1 e 100;
*  Entrada de palpites pelo usuário;
*  Indicação se o número secreto é maior ou menor;
*  Contagem de tentativas;
*  Possibilidade de desistir digitando `0`;
*  Validação de números fora do intervalo permitido;
*  Possibilidade de iniciar uma nova partida;
*  Validação da resposta para jogar novamente.

## Tecnologias

*  Python
*  Biblioteca `random`
*  Terminal / Console

## Conceitos praticados

### Funções

A lógica principal do jogo foi organizada dentro da função:

def jogar():

Isso permite executar uma nova partida sempre que necessário, sem precisar duplicar o código.

### Números aleatórios

A biblioteca `random` é utilizada para gerar o número secreto:

num_secreto = random.randint(1, 100)

### Estruturas de repetição

O `while` é utilizado para:

* validar o número informado;
* manter o jogo funcionando até o jogador acertar ou desistir;
* permitir iniciar novas partidas.

### Estruturas condicionais

`if`, `elif` e `else` são utilizados para verificar:

* se o jogador desistiu;
* se o palpite é menor que o número secreto;
* se o palpite é maior;
* se o jogador acertou;
* se a opção para jogar novamente é válida.

### Validação de entrada

O programa verifica se o número informado está dentro do intervalo permitido:

while num < 0 or num > 100:

O jogador pode informar números de `1` a `100` ou `0` para desistir.

### Contagem de tentativas

A variável `num_tentativas` registra a quantidade de tentativas realizadas pelo jogador.

## Como executar

Certifique-se de ter o **Python 3** instalado.

Clone o repositório:

git clone https://github.com/leonardosouzaaires4-crypto/python-fundamentos.git

Acesse a pasta do projeto:

cd python-fundamentos/jogo-adivinhacao

Execute o programa:

python adivinhe_o_numero.py

Em alguns ambientes, pode ser necessário utilizar:

python3 adivinhe_o_numero.py

## Exemplo de execução

JOGO DE ADIVINHAÇÃO

Digite um número entre 1 e 100 ou 0 para desistir: 50

O número secreto é maior.

Tente novamente: 75

O número secreto é menor.

Tente novamente: 63

Parabéns! Você acertou o número secreto com 3 tentativas.

Deseja jogar novamente? sim

### Desistindo da partida

O jogador pode digitar `0`:

Digite um número entre 1 e 100 ou 0 para desistir: 0

Você desistiu, mas o número secreto era: 87

### Número inválido

Caso seja informado um número fora do intervalo:

Digite um número entre 1 e 100 ou 0 para desistir: 150

Número inválido. Digite um número entre 1 e 100 ou 0 para desistir.

## Possíveis melhorias futuras

Algumas funcionalidades podem ser adicionadas conforme novos conceitos de Python forem estudados:

* [ ] Tratamento de erros com `try/except`;
* [ ] Sistema de níveis de dificuldade;
* [ ] Limite de tentativas;
* [ ] Sistema de pontuação;
* [ ] Ranking de melhores pontuações;
* [ ] Histórico de partidas;
* [ ] Melhor organização do código em diferentes módulos.

## Status

**Concluído — versão inicial**

O projeto poderá receber novas funcionalidades conforme novos conhecimentos de Python forem adquiridos.

---

Projeto desenvolvido durante meus estudos de **Python e lógica de programação**.
