num = int(input("Digite um numero inteiro:"))
soma = soma3 = soma5 = soma7 = 0


while num % 2 == 0:
    num = num/2
    soma = soma + 1
while num % 3 == 0 or num == 1 :
    num = num/3
    soma3 = soma3 + 1
while num % 5 == 0:
    num = num/5
    soma5 = soma5 + 1
while num % 7 == 0:
    num = num/3
    soma7 = soma7 + 1

print("multiplicidade:", soma, "^ 2 ||", soma3, "^ 3 ||", soma5, "^ 5 ||", soma7, "^ 7")