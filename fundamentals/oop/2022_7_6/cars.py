
#snake_case camelCase PascalCase
#use pascalcase when naming

class Car:
    creator = "Tyler"
    # builds instance of the house. The color default is blue if no color is put below.
    def __init__(self, make, model, color='blue'):
        self.make = make
        self.model = model
        self.color = color
        self.is_running = False
        return self
    
    def turn_on(self):
        self.is_running = True
        return self

    def info(self):
        print("*"*80)
        print(f"creator: {self.creator}")
        print(f"make: {self.make}")
        print(f"make: {self.model}")
        print(f"make: {self.color}")
        return self

    def drive(self):
        if self.is_running:
            print("driving driving driving")
        else:
            print("cannot drive because I'm not started")
        return self

    #this says it is targeting the whole class
    @classmethod
    def change_creator(cls, new_creator):
        cls.creator = new_creator

    # we are grouping this function with the car so that we can call it from different files.
    @staticmethod
    def is_appropriate_color(color):
        color_list = ['blue', 'black', 'white']
        if color in color_list:
            return True
        else:
            return False

car_a = Car('toyota')
car_b = Car('tesla', 'model4', 'yellow')

# car_a = Car('toyota')
# car_b = Car('tesla',color='yellow',model='model4')

# print(car_a.make)
# print(car_b.make)

car_a.turn_on()
car_b.is_running = True

car_a.drive().turn_on().drive().info()

# car_a.drive()
# car_b.drive()

# print(car_a.is_running)
# print(car_b.is_running)

print(Car.is_appropriate_color(car_a.color))
print(Car.is_appropriate_color(car_b.color))


#because used "Car" it idd it for all the instances in the class
Car.change_creator("Brandon")

car_a.info()
car_b.info()