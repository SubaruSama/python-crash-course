# A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the
# change.
# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.

restaurant_foods = ('massa a bolonhesa', 'lasanha', 'frango a molho mostarda', 'pastel', 'brocolis salteado')

for food in restaurant_foods:
	print(f'Comidas no restaurante: {food}')

# print('Adicionando no cardapio uma nova comida: ')
# restaurant_foods[0] = 'arroz salteado'

restaurant_foods = ('arroz frito', 'lasanha', 'pastel', 'rolinho primavera', 'brocolis no vapor')

print('Houve uma troca no cardapio: ')
for food in restaurant_foods:
	print(f'Comidas no restaurante: {food}')
