def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        raise ValueError("Invalid operator.")

def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("❌ Invalid number. Please enter a numeric value.")

def get_operator(prompt):
    while True:
        op = input(prompt)
        if op in "+-*/":
            return op
        else:
            print("❌ Invalid operator. Please use one of + - * /.")

print("Welcome to the Basic Calculator!")
print("You can enter two numbers and an operator (+, -, *, /).\n")

while True:
    a = get_number("Enter 1st number: ")
    op = get_operator("Enter operator (+ - * /): ")
    b = get_number("Enter 2nd number: ")

    while op == "/" and b == 0:
        print("❌ Cannot divide by zero.")
        b = get_number("Enter a new second number: ")

    try:
        result = calculate(a, b, op)
        print(f"The result is {result}")
    except ValueError as e:
        print(f"Error: {e} \nLet's try that again")
    
    again = input("Do you want to calculate again? (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye! 👋")
        break