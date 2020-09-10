# Build a v1 of Calculator that adds
# Refactor to add in other factors

print("Hello and welcome to the calculator")

# methods that return calculation

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# make a choice, call the method and return the output and print to screen
print("What would you like to do today?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# menu system to select add, sub, mult,div
while True:
    choice = input("Enter input number 1/2/3/4")

    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number"))
        num2 = float(input("Enter second number"))
        if choice == "1":
            print(add(num1, num2))
        elif choice == "2":
            print(subtract(num1, num2))
        elif choice == "3":
            print(multiply(num1, num2))
        elif choice == "4":
            print(divide(num1, num2))
        break
    else:
        print("You did not enter valid input")
