class Car:
    started = False   # started and wheels are class variables
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand    #brand model year are instance variables
        self.model = model
        self.year = year
        self.disc = f"{brand} {model} - {year}"

    def start(self):
        if self.started:
            print("car is started already.")
        else:
            self.started = True
            print("car started")

    def stop(self):
        if self.started:
            self.started = False
            print("car stopped")
        else:
            print("car already stopped")

    def talk(self):
        print("Every car has atleast {} wheels.".format(Car.wheels))
        print(f"and this {self.disc} has {self.wheels} wheels.")


car_1 = Car("BMW", "M4", 2018)
car_2 = Car("Tesla", "p1000", 2017)
car_1.wheels = 6
car_1.talk()
car_2.talk()
