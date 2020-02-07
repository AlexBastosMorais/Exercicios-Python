#Faça um programa que receba duas notas digitadas pelo usuário. 
#Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.  

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
total = (nota1 + nota2) / 2
if total >= 6:
    print("Sua nota é {}, parabéns você foi aprovado.".format(total))
else:
    print("Sua nota é {}, Sinto muito você foi reprovado.".format(total))


