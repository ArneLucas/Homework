def add(*args):
    print(args[0])  # since the args is a tuple, you can use index

    sum = 0
    for n in args:
        sum += n
    print(sum)


# add(1, 2, 3, 4, 5, 6)

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")  # .get doesn't return an error when non existent
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


my_car = Car(make="Subaru", model="Impreza")
print(my_car.make)
