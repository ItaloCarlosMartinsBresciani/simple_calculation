import math
a = int(input("Digite o valor de A:"))
b = int(input("Digite o valor de B:"))
c = int(input("Digite o valor de C:"))
delta = b**2 - (4 * a * c)
 
if delta == 0:
    raiz0 = (-b + math.sqrt(delta))/2*a
    print("a raiz desta equação é", raiz0)
elif delta > 0:
    raiz1 = (-b + math.sqrt(delta))/2*a
    raiz2 = (-b - math.sqrt(delta))/2*a
    if raiz1<raiz2:
        print("as raízes da equação são", raiz1, "e" , raiz2)
    else:
        print("as raízes da equação são", raiz2, "e" , raiz1)
elif delta < 0:
    print("esta equação não possui raízes reais")

