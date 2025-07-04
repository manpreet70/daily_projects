from calculator.calculator_core import calculate, get_number, get_operator, log_operation, view_history

def main():
    print("Welcome to the Basic Calculator!")
    print("You can enter two numbers and an operator (+, -, *, /).\n")

    while True:
        a = get_number("Enter 1st number: ")
        op = get_operator("Enter operator (+ - * /): ").strip()
        b = get_number("Enter 2nd number: ")

        while op == "/" and b == 0:
            print("❌ Cannot divide by zero.")
            b = get_number("Enter a new second number: ")

        try:
            result = calculate(a, b, op)
            print(f" {a}{op}{b} = {int(result) if result.is_integer() else result}")
            log_operation(a, b, op, result)
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("🔁 Let’s try that again...\n")
            continue

        next_action = input("Do you want to\n (c) Calculate again\n (h) History\n (q) Quit ").strip().lower()
        
        
        if next_action == "h":
            print("\n📜 Calculation History")
            view_history()
        elif next_action == "q":
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    main()