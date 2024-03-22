fat = int(input("Digite o valor de n:"))

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
    print(valor)
else:
    print(valor)

