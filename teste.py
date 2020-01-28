print("Bem vindo a calculadora ")
print("Qual a operação")
op = input(" ")
if op == "+":
    n1= float(input("Digite o primeiro numero: "))
    n2= float(input("digite o segundo numero: "))
    soma = n1 + n2
    print(soma)
elif op == "-":
    n1= float(input("Digite o primeiro numero: "))
    n2= float(input("digite o segundo numero: "))
    subtrair = n1 - n2
    print(subtrair)
elif op == "*":
    n1= float(input("Digite o primeiro numero: "))
    n2= float(input("digite o segundo numero: "))
    mult = n1 * n2
    print(mult)
elif op == "/":
    n1= float(input("Digite o primeiro numero: "))
    n2= float(input("digite o segundo numero: "))
    div = n1 / n2     
    print(div)


