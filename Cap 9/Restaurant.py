class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 12

    def describe_restaurant(self):
        print(f'The {self.restaurant_name} serves food from {self.cuisine_type} cuisine!')

    def open_restaurant(self):
        print(f'The restaurant {self.restaurant_name} is open!')

    def set_number_served(self, quantity: int) -> int:
        self.number_served = quantity

    def increment_number_served(self, clientes_served: int) -> None:
        self.number_served += clientes_served

    def get_clients_served(self) -> int:
        return self.number_served