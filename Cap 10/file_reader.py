extension = '.txt'
filename = f'pi_million_digits{extension}'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f'{pi_string[:52]}...')
print(len(pi_string))

bday = input('Enter your birthday, in the form ddmmyy: ')
if bday in pi_string:
    print('Your bday appears in the first million digits of pi!')
else:
    print('Your bday does not appear in the first million digits of pi :<')