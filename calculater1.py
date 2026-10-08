
def calculate(num1, operator, num2):
    
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operator.")


def parse_input(user_input):
   
    parts = user_input.split()

    if len(parts) != 3:
        raise ValueError("Enter input in this format: number operator number")

    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator not in ["+", "-", "*", "/"]:
        raise ValueError("Operator must be +, -, *, or /.")

    return num1, operator, num2


def main():
    while True:
        print("\n--- Calculator ---")
        print("1. Calculate")
        print("2. Clear")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            user_input = input("Enter calculation (e.g., 10 + 5): ")

            try:
                num1, operator, num2 = parse_input(user_input)
                result = calculate(num1, operator, num2)
                print("Result:", result)

            except ValueError as error:
                print("Invalid input:", error)

            except ZeroDivisionError as error:
                print("Error:", error)

        elif choice == "2":
            print("Calculator cleared.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
