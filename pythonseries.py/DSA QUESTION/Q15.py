num1 = int(input("Enter first number: ").strip())
num2 = int(input("Enter second number: ").strip())

op = input("Enter any operater (+, -, *, %, /): ")

if op == '+':
    print("Result = ", num1 + num2)
elif op == '-':
    print("Result = ", num1 - num2)
elif op == '*':
    print("Result = ", num1 * num2)
elif op == '%':
    if num2 != 0:
      print("Result = ", num1 % num2)
    else:
        print("Error...")
elif op == '/':
    if num2 != 0:
        print("Result = ", num1 / num2)
    else:
        print("Error...")
else:
    print("Invalid choise....")
