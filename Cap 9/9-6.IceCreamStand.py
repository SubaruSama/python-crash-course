'''
An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand , and call this method.
'''

from Restaurant import Restaurant

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name: str, cuisine_type: str, flavors: list):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_icecream_flavors(self):
        print(f'We have those flavors: ')
        for flavor in self.flavors:
            print(flavor)

ice_cream_stand = IceCreamStand(
    restaurant_name='Ice Cream Cone', 
    cuisine_type='ice cream', 
    flavors=[
        'strawberry', 
        'mango', 
        'lime', 
        'pineapple']
)
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.display_icecream_flavors()