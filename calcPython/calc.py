def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    else:
        return a / b

def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print("Resultado:", adicao(num1, num2))
            elif escolha == '2':
                print("Resultado:", subtracao(num1, num2))
            elif escolha == '3':
                print("Resultado:", multiplicacao(num1, num2))
            elif escolha == '4':
                print("Resultado:", divisao(num1, num2))
        elif escolha == '5':
            print("Saindo da calculadora. Até logo!")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

# Executar a calculadora
calculadora()
