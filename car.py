"""A class that can be used to represent a car."""
class Car():
    #"""Initialize attributes to describe a car."""
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_adometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer(self, miles):
        """Add the given amount of to the odometer reading."""
        self.odometer_reading += miles
        
class Battery():
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=85):
        """Initialize  the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + " -kwh battery." )
        
    def get_range(self, range= 240 or 270):
        """Print a statement about the range this battery provides."""
        #range = 240
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class. 
        Then initialize attributes specific to an electric car. 
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_adometer(23500)
# my_used_car.read_odometer()

# my_new_car = Car('audi', 'a4', 2020)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_adometer(23)
# my_new_car.read_odometer()
