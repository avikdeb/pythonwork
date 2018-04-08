def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def print_choice():
    print("Select Operation:")
    print("[A] Add")
    print("[S] Subtract")
    print("[M] Multiply")
    print("[D] Divide")


def input_choice():
    choice = input("Enter choice - A or S or M or D \n")
    return choice

def input_processing():

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num_list = [num1, num2]
    return num_list

def calculation(choice, num_list):

    i = num_list[0]
    j = num_list[1]
    if choice == "A":
        print(i, "+", j, "=", add(i, j))
    elif choice == "S":
        print(i, "-", j, "=", subtract(i, j))
    elif choice == "M":
        print(i, "X", j, "=", multiply(i, j))
    elif choice == "D":
        print(i, "/", j, "=", divide(i, j))
    else:
        print("[ERROR] Invalid input")
