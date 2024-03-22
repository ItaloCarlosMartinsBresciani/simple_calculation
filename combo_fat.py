def fatorial():
    valor = 1
    while valor != 0:
        fat = int(input("Digite um fatorial(digite 0 para sair):"))
        if fat == 0:
            valor = 0
            fat = 1 
        control = fat - 1
        while control > 0:
            fat = fat * control
            control = control - 1     
        print(fat)
fatorial()