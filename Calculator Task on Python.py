# add two numbers
def add(x, y):
    return x + y

# subtract two numbers
def subtract(x, y):
    return x - y

#  multiply two numbers
def multiply(x, y):
    return x * y

# divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Display the user
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get  input
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input! Please select a valid operation.")


calculator()
