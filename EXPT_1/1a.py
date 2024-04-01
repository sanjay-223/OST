while True:
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero.")
            continue
    else:
        print("Invalid operation.")
        continue

    print("Result: ", result)

    another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if another_calculation != 'yes':
        break
