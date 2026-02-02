print('========== CALCULADORA =============')


numero1 = int(input("Digite seu primeiro numero: "))
numero2 = int(input("Digite seu segundo numero: "))

operacao = input("Qual operacao voce deseja fazer? (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
    print("Resultado:", resultado)

elif operacao == "-":
    resultado = numero1 - numero2
    print("Resultado:", resultado)

elif operacao == "*":
    resultado = numero1 * numero2
    print("Resultado:", resultado)

elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    else:
        print("Erro: divisao por zero")

else:
    print("Operacao invalida")
