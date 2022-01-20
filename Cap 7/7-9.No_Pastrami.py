'''
Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders . Make sure no pastrami sandwiches end up
in finished_sandwiches .
'''

sandwich_orders = [
    'pastrami', 
    'sanduiche de atum',
    'farroupilha', 
    'sanduiche vegetariano', 
    'pastrami', 
    'sanduiche vegano', 
    'sanduiche de queijo com mortadela', 
    'pastrami'
]
finished_sandwiches = []

print(f'Sanduiches a serem feitos: {len(sandwich_orders)}')
print('Nossa loja nao possui mais pastrami...')
print('--- Retirando todas as ordens que sejam de pastrami ---')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(f'Sanduiches a serem feitos: {len(sandwich_orders)}')

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f'Fiz o seu sanduiche sabor {finished_sandwich}')
    finished_sandwiches.append(finished_sandwich)

print('\nSanduiches feitos: ')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

print(f'\nSanduiches a serem feitos: {len(sandwich_orders)}')