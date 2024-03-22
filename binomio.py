n = int(input("Digite o valor de n:"))
k = int(input("Digite o valor de k:"))

def fatorial(fat):
          
    controle = 1
    num = fat - controle
    valor = num * fat
    controle += 1

    while controle < fat:
            num = fat - controle
            valor *= num 
            controle += 1

    if num == 0 or num == -1:
        valor = 1
        return(valor)
    else:
        return(valor)   

def calc(prim, seg):
    bin = fatorial(prim)/(fatorial(seg)*fatorial(prim-seg))
    return bin
print(calc(n,k))

     