'''
Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a
day of business.
'''

from Restaurant import Restaurant

restaurant = Restaurant('TarTar Binks', 'Thai')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(10)
restaurant.increment_number_served(20)
print(f'Clientes served: {restaurant.get_clients_served()}')