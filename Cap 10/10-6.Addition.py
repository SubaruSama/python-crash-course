"""
One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int , you’ll get a TypeError . Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
"""
'''10.7'''

while True:
    try:
        number1 = int(input("Enter number 1: "))
        number2 = int(input("Enter number 2: "))
        result = number1 + number2

        if (number1 or number2) == 'q':
            print("Exiting...")
            break

        if (number1 or number1) is int:
            result = number1 + number2

        print(f"Result: {result}")

    except (TypeError):
        print("Only int type allowed")