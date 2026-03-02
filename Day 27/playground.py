# def add(*sum):
#     result = 0
#     for n in sum:
#         result+=n
#     print(result)
#
# add(2,55,6,4,3,2,33,555,3)
#
# def calculation(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculation(3, add=9, multiply=45)
#
#
# class Car:
#
#     def __init__(self, **kw):
#         self.model = kw.get("model")
#         self.colour = kw.get("colour")
#         self.make = kw.get("make")
#
# my_car = Car(model="camry", colour="red", make="toyota")
#
# print(my_car.model)
#

def add(*args):
    my_sum = 0
    for i in args:
        my_sum += i
    print(my_sum)

add(2,33,444,4,4, 445,6,6 ,656,445, 45, 46)

def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R")

print(my_car.colour)