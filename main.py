"""A simple command-line calculator."""


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        raise ValueError("Cannot divide by zero")
    return first / second


def is_numeric(value):
    """Return True when value can be converted to a number."""
    try:
        float(value)
        return True
    except ValueError:
        return False


def main():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    print("Simple Calculator")
    print("Enter q at any prompt to quit.")

    while True:
        first_input = input("First number: ")
        if first_input.lower() == "q":
            break
        if not is_numeric(first_input):
            print("Error: Please enter a numeric value.")
            continue

        operator = input("Operation (+, -, *, /): ")
        if operator.lower() == "q":
            break
        if operator not in operations:
            print("Invalid operation.")
            continue

        second_input = input("Second number: ")
        if second_input.lower() == "q":
            break
        if not is_numeric(second_input):
            print("Error: Please enter a numeric value.")
            continue

        first = float(first_input)
        second = float(second_input)
        try:
            result = operations[operator](first, second)
        except ValueError as error:
            print(f"Error: {error}")
            continue

        print(f"Result: {result}")


if __name__ == "__main__":
    main()
