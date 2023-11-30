
from time import time

def execution_time_and_count_attributes(func):
    def wrapper(a):
        start_time = time()

        result = func(a)

        end_time = time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")

        return result
    return wrapper

class Brand:
    def __get__(self, instance, owner):
         return instance._brand
    def __set__(self, instance, value):
        if isinstance(value,str):
            instance._brand = value
            print('s')
        else:
            raise ValueError('brand must be a string.')
        
class Model:
    def __get__(self, instance, owner):
        return instance._model
    def __set__(self, instance, value):
        if isinstance(value,str):
            instance._model = value
        else:
            raise ValueError('Model ,must be a string')

class Year:
    def __get__(self, instance, owner):
        return instance._year
    def __set__(self, instance, value):
        if isinstance(value,int):
            instance._year = value
        else:
            raise ValueError('Year must be a integer')

class Car:
    brand = Brand()
    model = Model()
    year = Year()
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print("print somthing until go init method")
        return instance
    # self-ში გადაეცემა ობიექტი, ზევით შექმნილი instance
    def __init__(self, brand, model, year):
        print("Initializing Car instance")

        self.brand = brand
        self.model = model
        self.year = year 

    @execution_time_and_count_attributes
    def count_attributes(self):
        attributes = ''
        count = len(vars(self))
        for key, _ in vars(self).items():
                attributes += f'{key}, '
        attributes = attributes[:-2] + '.'
                
        return f'Number of attributes: {count}.\nAttributes names: {attributes}'


car1 = Car("Toyota", "Corolla", 2023)
print(f"Car: {car1.brand} {car1.model} ({car1.year})")
# # car1.brand = 3

result = car1.count_attributes()
print(result)
# 
print(car1.brand)


print(car1.brand)

#2.შექმენით დეკორატორი, რომელიც დაითვლის და დაგვიბეჭდავს დროს, თუ რა დრო დასჭრიდა ობიექტის მეთოდის შერულებას და დაგვიწერს რა ატრიბუტები აქვს გადმოცემული ობიექტს
#3.Car კლასს დაუმატეთ თითოეული ატრიბუტისთვის set და get ფუნქტორი მათი ცვლილებებისთვის და დაამატეთ ვალიდაციები თითოეული ატრიბუტისთვის
