# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers
# in your list

multiples_of_three = [value for value in range(3, 31) if value % 3 == 0]

for number in multiples_of_three:
	print(f"Number divisible by 3: {number}")
