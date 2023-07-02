# Função para realizar a operação de adição
def adicao(a, b):
    return a + b

# Função para realizar a operação de subtração
def subtracao(a, b):
    return a - b

# Função para realizar a operação de multiplicação
def multiplicacao(a, b):
    return a * b

# Função para realizar a operação de divisão
def divisao(a, b):
    return a / b

# Função principal que recebe a entrada do usuário e realiza a operação escolhida
def calculadora():
    print("Escolha a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Digite o número da operação desejada: ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == '1':
        resultado = adicao(num1, num2)
        print("O resultado da adição é:", resultado)
    elif operacao == '2':
        resultado = subtracao(num1, num2)
        print("O resultado da subtração é:", resultado)
    elif operacao == '3':
        resultado = multiplicacao(num1, num2)
        print("O resultado da multiplicação é:", resultado)
    elif operacao == '4':
        if num2 != 0:
            resultado = divisao(num1, num2)
            print("O resultado da divisão é:", resultado)
        else:
            print("Não é possível dividir por zero!")
    else:
        print("Operação inválida!")

# Chamar a função da calculadora
calculadora()
