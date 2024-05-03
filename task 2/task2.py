def calculator():
    print("Simple Calculator")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    valid_choices = [1, 2, 3, 4]
    operations = {
        1: ("+", num1 + num2),
        2: ("-", num1 - num2),
        3: ("*", num1 * num2),
        4: ("/", num1 / num2 if num2 != 0 else None)
    }

    print("\nSelect Operation:")
    for index, operation in operations.items():
        print(f"{index}. {operation[0]}")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if choice not in valid_choices:
        print("Invalid choice. Please enter a number between 1 and 4.")
        return

    operation, result = operations[choice]
    if result is None:
        print("Error: Cannot divide by zero.")
        return

    print("\nResult:")
    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()