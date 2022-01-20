# Make a list of the nyumbers from one to one million, and the use
# min() and max() to make sure your list actually starts at one and ends at
# one million. Also, use the sum() to see how quickly python can add a million numbers

one_million = []

for i in range(1, 1000001):
	one_million.append(i)

print(f"min() of one_million: {min(one_million)}")
print(f"max() of one_million: {max(one_million)}")
print(f"sum() of one_million: {sum(one_million)}")
