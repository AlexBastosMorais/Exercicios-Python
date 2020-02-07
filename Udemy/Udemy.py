#Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade. 
idade = int(input("Qual a sua idade: "))
if idade >= 18:
    print("Usuario possui {} anos, por tanto ele é maior de idade.".format(idade))
else:
    print("Usuario possui {} anos, por tanto ele é menor de idade.".format(idade))