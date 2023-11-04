class Calculator:
    def calculate(self, num1, num2):
        pass


class Add(Calculator):
    def calculate(self, num1, num2):
        return num1 + num2


class Subtract(Calculator):
    def calculate(self, num1, num2):
        return num1 - num2


class Multiply(Calculator):
    def calculate(self, num1, num2):
        return num1 * num2


class Divide(Calculator):
    def calculate(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Cannot divide by zero!")


# Example usage
addition = Add()
subtraction = Subtract()
multiplication = Multiply()
division = Divide()

print("Addition:", addition.calculate(5, 2))
print("Subtraction:", subtraction.calculate(5, 2))
print("Multiplication:", multiplication.calculate(5, 2))
print("Division:", division.calculate(5, 2))