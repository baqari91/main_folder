import csv
# class Car:
#     discount_rate = 0.8
#     all_cars = []
#
#     def __init__(self, name: str, price: float, number=0):
#
#         assert len(name) > 0, "You entered empty string!"
#         assert len(name) < 15, "Entered name is too long!"
#         assert price > 0, "Price must be Positive number!"
#
#         self.__name = name
#         self.price = price
#         self.number = number
#
#         Car.all_cars.append(self)
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         assert len(value) > 0, "You entered empty string!"
#         assert len(value) < 15, "Entered name is too long!"
#
#         self.__name = value
#
#
#     def total_price(self):
#         return self.price * self.number
#
#     def calculate_discount(self):
#         return self.price * self.discount_rate
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.__name}, {self.price}, {self.number})"
#
#     @classmethod
#     def create_object(cls):
#         with open("cars.csv", "r") as file:
#             cars_info = list(csv.DictReader(file))
#
#             for car in cars_info:
#                 Car(
#                     name=car["name"],
#                     price=float(car["price"]),
#                     number=float(car["quantity"])
#                 )
#
#     @staticmethod
#     def check_if_odd(x):
#         return x % 2 == 0
#
#
#     def __check_somthing(self):
#         pass
#
#     def idontknow(self):
#         self.__check_somthing()
#         print("Result")
#
# class Electric_Car(Car):
#     pass
#
# car1 = Car("BMW", 3000)
# car1.name = "Mazda"
#


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         # print("Printed By Decorator")
#         # print(args)
#         print(kwargs)
#         num1 = kwargs["x"]
#         num2 = kwargs["y"]
#         print(num1)
#         print(num2)
#         # num1 = args[0] + 10
#         # num2 = args[1] + 10
#         # func(num1, num2)
#     return wrapper
#
#
#
# @decorator
# def test_for_decorator(x, y):
#     print(x+y)
#
# test_for_decorator(x=10, y=20)



# class TestFunctor:
#     def __call__(self, *args, **kwargs):
#         print("Test Functor")
#         print(args)
#
#
#
# test_functor = TestFunctor()
# test_functor(1, 2, 3 ,4 ,5 ,6)


# class TestDescriptor:
#     def __get__(self, instance, owner):
#         print(f"Getting Value: {instance.value}")
#         return instance.value
#
#     def __set__(self, instance, value):
#         print(f"Setting Value: {value}")
#         instance.value = value
#
#     def __delete__(self, instance):
#         print("Deleting Values")
#         del instance.value
#
#
# class MyClass:
#     def __init__(self, value):
#         self.value = value
#
#     descriptor = TestDescriptor()
#
# obj = MyClass(value=30)
# desc = obj.descriptor
# print(desc)
# obj.descriptor = 100
# del obj.descriptor
# print(obj.descriptor)


# class Car:
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls)
#         return instance
#
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
# print(type(Car))
# print(type(int))
#
# car1 = Car("BMW", "F30")


# def init(self, brand, model):
#     self.brand = brand
#     self.model = model
#
# def print_values(self):
#     return f"Brand: {self.brand}, Model: {self.model}"
#
# Car = type('Car', (object,),{
#     '__init__': init,
#     'print_values': print_values
# })
#
# car1 = Car(brand = "BMW", model = "F30")
# print(car1.print_values())



class Car(type):
    def __new__(cls, name, bases, dct):
        instance = super().__new__(cls, name, bases, dct)
        return instance


class ElectricCar(metaclass=Car):
    def __init__(self, brand):
        self.brand = brand

    def print_brand(self):
        return self.brand


elCar = ElectricCar("Tesla")
print(elCar.print_brand())

print(type(ElectricCar))
print(type(Car))