large = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))
i = 1
control = large
while altura >= i:
    while large >= i:
        large = large - 1
        print("#", end="")
        
    large = control
    altura = altura - 1   
    print(end="\n")