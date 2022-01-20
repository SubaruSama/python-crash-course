pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print('You order a {crust} crust pizza with the following toppings:'.format(crust=pizza['crust']))

for topping in pizza['toppings']:
    print(f'\t{topping}')
