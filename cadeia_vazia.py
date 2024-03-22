line = int(input("Digite a largura:"))
column = int(input("Digite a column:"))
i = 1
control = line
control2 = column
while column >= i:
    while line >= i:
        if line == control or column == control2 or line == 1 or column == 1:
            print("#", end="")
        else:
            print(end=" ")
        line = line - 1
                
    line = control
    column = column - 1   
    print(end="\n")