#Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.   
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))

op = input('Escolha uma operação: ')
if op == '+':
    soma = n1 + n2
    print('Voce escolheu somar {} + {}, seu resultado é esse:{} '.format(n1,n2,soma))

elif op == '-':
    menos = n1 - n2
    print('Voce escolheu subtrair {} - {}, seu resultado é esse:{} '.format(n1,n2,menos))

elif op == '*':
    mult = n1 * n2 
    print('Voce escolheu multiplicar {} * {}, seu resultado é esse:{} '.format(n1,n2,mult))       

elif op == '/':
    dividir = n1 / n2
    print('Voce escolheu dividir {} / {}, seu resultado é esse: {}'.format(n1,n2,dividir))

else:
    print('Invalido.')