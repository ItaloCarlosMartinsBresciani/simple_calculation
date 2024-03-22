num = int(input("Digite um número inteiro:"))
i = 0
control = num
repetiu = False

while control != 0:
    if (i == 0):
        resto = control % 10
        control = num//10
        numAnterior = resto  
        i = 1
    else:
        resto = control % 10
        control = control // 10 
        
        if (numAnterior == resto):
            repetiu = True
        else:
            numAnterior = resto

if (repetiu == True):
    print("sim")
else:
    print("não")
        


