a = float(input("Enter first number: "))
op = input("Enter operation (+ - * / ** %): ")
b = float(input("Enter second number: "))
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print(a / b)
elif op == "**":
    print(a ** b)
elif op == "%":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print(a % b)
else:
    print("Unknown operation")
