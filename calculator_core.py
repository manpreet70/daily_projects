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
