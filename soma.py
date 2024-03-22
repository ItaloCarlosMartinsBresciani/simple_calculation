valor = int(input("Digite um numero inteiro:"))
inteiro = valor
soma = 0
while inteiro != 0:
    resto = inteiro % 10
    inteiro = inteiro // 10 
    soma += resto
print(soma)