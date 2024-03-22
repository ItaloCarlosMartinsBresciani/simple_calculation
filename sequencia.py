val = 1
lista = []

while val !=0:
    val = int(input("Digite um valor(0 pra terminar)"))
    lista.append(val)


control = len(lista) 

while control > 0:

    print(lista[control-1])
    control = control - 1


