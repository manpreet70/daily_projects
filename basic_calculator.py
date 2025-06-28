from calculator_core import calculate, get_number, get_operator

def main():
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

if __name__ == "__main__":
    main()