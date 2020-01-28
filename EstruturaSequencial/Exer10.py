print ("---2 inteiros e um Real----")
fun = input ()
if fun ==  "a":
    n1 = int(input("Informe um valor inteiro: "))
    n2 = int(input("Informe outro valor inteiro: "))
    a = (n1 * 2) + (n2 / 2)
    print("O dobro do primeiro com a metade do segundo é igual: ", a)

elif fun == "b":
    n1 = int(input("Informe um valor inteiro: "))
    n3 = float(input("Informe um valor real: "))
    b = (n1 * 3) + n3
    print("A soma do triplo do primeiro com o terceiro: ", b)

elif fun == "c":
    n3 = float(input("Informe um valor real: "))
    c = n3 * n3 * n3
    print("O terceiro elevado ao cubo: ", c)


