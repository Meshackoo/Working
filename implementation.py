def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        raise ValueError("Division by zero is not allowed")
    return num1 / num2

def main():
    operation = input("Enter operation (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    try:
        if operation == '+':
            result = addition(num1, num2)
        elif operation == '-':
            result = subtraction(num1, num2)
        elif operation == '*':
            result = multiplication(num1, num2)
        elif operation == '/':
            result = division(num1, num2)
        else:
            raise ValueError("Invalid operation")

        print("Result: ", result)

    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()