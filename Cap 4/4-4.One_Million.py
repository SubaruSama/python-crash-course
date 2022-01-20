# Make a list of the numbers from one to one million, and then use a for loop 
# to print the numbers. (If the output is taking too long, stop it by pressing ctrl-c

one_million = []
for i in range(1, 1000001):
	one_million.append(i)

for number in one_million:
	print(number)
