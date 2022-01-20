'''
7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari-
ous sandwiches. Then make an empty list called finished_sandwiches . Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
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

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f'Fiz o seu sanduiche sabor {finished_sandwich}')
    finished_sandwiches.append(finished_sandwich)

print('\nSanduiches feitos: ')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

print(f'\nSanduiches a serem feitos: {len(sandwich_orders)}')