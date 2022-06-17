def add_numbers(array):
    sum = 0
    for number in array:
        sum = number + sum
    return sum
print(add_numbers())


def subtract_two_numbers(num1, num2):
    return num1 - num2


def multiply_two_numbers(num1, num2):
    return num1 * num2


def divide_two_numbers(num1, num2):
    return num1 / num2


quit = False
while not quit:
    user_input = input("What operation would you like to do? ").lower()
    if user_input == "quit":
        quit = True
    elif user_input == "add":
        amount = int(input())



        num1 = int(input("First number"))
        num2 = int(input("Second number"))
        print(add_numbers(num1, num2))
    elif user_input == "subtract":
        num1 = int(input("First number"))
        num2 = int(input("Second number"))
        print(subtract_two_numbers(num1, num2))
    elif user_input == "multiply":
        num1 = int(input("First number"))
        num2 = int(input("Second number"))
        print(multiply_two_numbers(num1, num2))
    elif user_input == "divide":
        num1 = int(input("First number"))
        num2 = int(input("Second number"))
        print(divide_two_numbers(num1, num2))
    else:
        print("Sorry, that response is invalid.")

print("Thank you for using this calculator.")
