class Car:
    quantity_instances_created = 0

    def __init__(self, make: str, year: int, model: str):
        self.make = make
        self.year = year
        self.model = model
        self.odomoter_reading = 0
        Car.quantity_instances_created += 1

    @classmethod
    def get_quantity_instances(cls) -> int:
        return Car.quantity_instances_created

    def get_descriptive_name(self) -> str:
        return f'{self.make.title()} {self.year} {self.model.title()}'

    def read_odomoter(self) -> None:
        print(f'This car has {str(self.odomoter_reading)} miles on it')

    def update_odometer(self, mileage: int) -> None:
        '''
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        '''
        if mileage >= self.odomoter_reading:
            self.odomoter_reading += mileage
        else:
            print('Hey, you can\'t roll back and odometer!')

    def incremente_odometer(self, miles: int) -> None:
        if miles < 0:
            print('You can\'t update negatively miles')
            return

        self.odomoter_reading += miles

class ElectricCar(Car):
    '''
    Represents aspects of a car, specific to electric values.
    '''
    def __init__(self, make: str, year: int, model: str):
        super().__init__(make, year, model)
        self.battery = Battery()

class Battery():
    '''
    A simple attempt to model a battery for an electric car.
    '''
    def __init__(self, battery_size=70) -> None:
        self.battery_size = battery_size

    def describe_battery(self) -> None:
        print(f'This car has a {str(self.battery_size)}-kWh battery.')

    def get_range(self) -> None:
        '''Print a statement about the range this battery provides.'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = f'This car can go approx {str(range)}'
        message += ' miles on a full charge.'
        print(message)


my_new_car = Car(make='Subaru', model='XZ', year=2002)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odomoter()
my_used_car = Car(make='audi', model='a4', year=2016)
my_used_car.read_odomoter()
my_tesla = ElectricCar('tesla', 2016, 'model s')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print(f'Quantas instancias foram criadas ate agora: {Car.get_quantity_instances()}')