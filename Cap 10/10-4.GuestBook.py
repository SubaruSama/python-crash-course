"""
Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""

filename = 'guest_book.txt'
i = 0

with open(filename, 'w') as file:
    if file.writable():
        while i <= 10:
            guest_name = input('What is your name?: ')
            print(f'Hello {guest_name}!')
            file.write(f'{guest_name}\n')
            i += 1