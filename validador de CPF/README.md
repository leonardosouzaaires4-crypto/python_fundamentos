Validador de CPF em Python

Projeto desenvolvido em Python como parte dos estudos de fundamentos da linguagem e lógica de programação.

O programa recebe um CPF informado pelo usuário, remove caracteres de formatação, verifica sua estrutura e calcula os dígitos verificadores para determinar se o CPF possui uma combinação válida.

Objetivo

Praticar conceitos de programação utilizando Python, principalmente:

Funções
Manipulação de strings
Estruturas condicionais
Operadores matemáticos
Listas e iteradores
Validação de dados
Geração e comparação de valores
Uso de funções integradas da linguagem

Funcionalidades

O programa realiza as seguintes operações:

Recebe o CPF informado pelo usuário;
Remove automaticamente caracteres que não sejam números;
Verifica se o CPF possui 11 dígitos;
Identifica CPFs compostos pelo mesmo dígito;
Calcula o primeiro dígito verificador;
Calcula o segundo dígito verificador;
Compara os dígitos calculados com os informados;
Informa se o CPF é válido ou inválido.

Tecnologias

Python 3
Terminal / Console
Como funciona

O programa segue o seguinte fluxo:

Entrada do CPF
      |
      v
Remoção de caracteres não numéricos
      |
      v
Verificação da quantidade de dígitos
      |
      v
Verificação de dígitos repetidos
      |
      v
Cálculo do primeiro dígito verificador
      |
      v
Cálculo do segundo dígito verificador
      |
      v
Comparação dos dígitos
      |
      v
CPF válido ou inválido

Como executar

Certifique-se de ter o Python 3 instalado.

Clone o repositório:

git clone https://github.com/leonardosouzaaires4-crypto/python_fundamentos.git

Acesse a pasta do projeto:

cd python_fundamentos/validador de CPF

Execute o programa:

python validador_CPF.py

Em alguns ambientes, pode ser necessário utilizar:

python3 validador_CPF.py

Exemplos de execução

Digite o CPF para validação: 529.982.247-25
CPF válido.

O programa também aceita o CPF sem formatação:

Digite o CPF para validação: 52998224725
CPF válido.

CPF com quantidade incorreta de dígitos
Digite o CPF para validação: 123456
CPF inválido. O CPF deve conter 11 dígitos.
CPF inválido.

CPF com todos os dígitos iguais
Digite o CPF para validação: 111.111.111-11
CPF inválido. Todos os dígitos são iguais.
CPF inválido.

Conceitos praticados

Funções

A lógica de validação foi organizada dentro da função:

def validar_cpf(cpf):

Isso permite concentrar as regras de validação em uma única estrutura.

Manipulação de strings

A função:

''.join(filter(str.isdigit, cpf))

é utilizada para remover caracteres que não sejam números.

Dessa forma, entradas como:

529.982.247-25

são convertidas para:

52998224725

Validação de tamanho

O programa verifica se o CPF possui exatamente 11 dígitos:

if len(cpf) != 11:

Verificação de números repetidos

O programa também verifica se todos os dígitos são iguais:

if cpf == cpf[0] * 11:

Essa condição impede que sequências como 11111111111 sejam consideradas válidas.

Cálculo dos dígitos verificadores

Os dois últimos dígitos do CPF são calculados a partir dos demais números utilizando operações matemáticas e pesos específicos.

O programa então compara os valores calculados com os dois últimos dígitos informados pelo usuário.

Possíveis melhorias futuras

Adicionar tratamento de erros com try/except;
Separar a lógica de validação das mensagens exibidas ao usuário;
Criar funções específicas para cada etapa da validação;
Permitir a validação de vários CPFs em sequência;
Criar testes automatizados;
Criar uma interface gráfica ou aplicação web.

Status

Concluído — versão inicial.

O projeto poderá receber novas funcionalidades e refatorações conforme novos conceitos de Python forem estudados.

Projeto desenvolvido durante os estudos de Python e lógica de programação.
