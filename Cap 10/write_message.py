filename = 'programming.txt'

with open(filename, 'w') as file:
    if file.writable():
        file.write('I love programming.')