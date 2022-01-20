# A number raise to the third power is called a cube. For example, the cube of 2 is written
# as 2 ** 3 in python. Make a list of the first 10 cubes (that is, the cube of each
# integer from 1 through 10), and use a for lopp to print out the value of each cube

list_first_ten_cubes = []

for i in range(1, 11):
	list_first_ten_cubes.append(i ** 3)

for value in list_first_ten_cubes:
	print(value)
