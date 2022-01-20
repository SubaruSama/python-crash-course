filename = 'learning_python.txt'

with open(filename) as file:
    contents = file.read()
    print(contents)

with open(filename) as file:
    for line in file:
        print(line)

with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line)