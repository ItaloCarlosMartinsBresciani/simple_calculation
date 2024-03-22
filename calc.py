num1 = int(input("Digite um valor"))
num2 = int(input("Digite um valor"))
op = input("Digite a operacao (+ , -, * ou /):")
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("operador ou número não correspondente")