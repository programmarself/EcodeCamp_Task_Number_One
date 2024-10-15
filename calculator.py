# calculator.py
print("\n WELCOME TO  SIMPLE CALCULATOR \n")


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a / b

def calculator():
    while True:
        print("Options: add, subtract, multiply, divide, exit \n")
        operation = input("/n Choose an operation: ").lower()

        if operation == 'exit':
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input, please enter numbers only.")
            continue

        if operation == 'add':
            print(f"Result: {add(num1, num2)}")
        elif operation == 'subtract':
            print(f"Result: {subtract(num1, num2)}")
        elif operation == 'multiply':
            print(f"Result: {multiply(num1, num2)}")
        elif operation == 'divide':
            print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid operation, try again.")

if __name__ == "__main__":
    calculator()

print("\nDeveloped By : IRFAN ULLAH KHAN")
print("@2024")