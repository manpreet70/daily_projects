


def calculate(a, b, op):
    """Perform arithmetic operation on two operands based on the given operator."""
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
    """Prompt the user until a valid numeric input is provided."""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("❌ Invalid number. Please enter a numeric value.")


def is_valid_operator(op):
    """Check if the operator is one of the accepted arithmetic operators."""
    return op in "+-*/"

def get_operator(prompt):
    """Prompt the user until a valid operator is provided."""
    while True:
        op = input(prompt)
        if is_valid_operator(op):
            return op
        else:
            print("❌ Invalid operator. Please use one of + - * /.")


def log_operation(a, b, op, result):
    """Append a formatted calculation record to the log file."""
    with open("calculator_log.txt", "a") as f:
        f.write(f"{a} {op} {b} = {result}\n")

def view_history():
    """Read and print all entries from the calculator log file, if it exists."""
    try:
        with open("calculator_log.txt", "r") as f:
            history = f.readlines()
            if not history:
                print("🕘 No calculation history yet.")
            else:
                print("📜 Calculation History:")
                for line in history:
                    print(line.strip())
    except FileNotFoundError:
        print("🕘 No calculation history yet.")