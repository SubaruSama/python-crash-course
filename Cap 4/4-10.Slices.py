# Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# • Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
# • Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.

my_foods = ['massa com molho vermelho', 'pizza', 'calzone', 'hamburguer de grao de bico']

# Print the first three items:
print(f'The first three items are: {my_foods[0:3]}')
#for food in my_foods[0:4]:
#	print(f'The first three items are: {food}')

# Three items from the middle of the list
print(f'Three items from the middle of the list are: {my_foods[1:3]}')
#for food in my_foods[1:3]:
#	print(f'Three items from the middle of the list are: {food}')

# The last three items in the list are:
print(f'The last three items in the list are: {my_foods[1:]}')
#for food in my_foods[2:]:
#	print(f'The last three items in the list are: {food}')
