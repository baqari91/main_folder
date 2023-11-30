
from time import time

def execution_time_and_count_attributes(func):
    def wrapper(self, *args, **kwargs):
        start_time = time()

        result = func(self, *args, **kwargs)

        end_time = time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")

        return result
    return wrapper

class Brand:
    def __get__(self, instance, owner):
        return instance._brand
    
    def __set__(self, instance, value):
        if isinstance(value, str):
            instance._brand = value
        else:
            raise ValueError('Brand must be a string.')
        
class Model:
    def __get__(self, instance, owner):
        return instance._model
    
    def __set__(self, instance, value):
        if isinstance(value, str):
            instance._model = value
        else:
            raise ValueError('Model must be a string')

class Year:
    def __get__(self, instance, owner):
        return instance._year
    
    def __set__(self, instance, value):
        if isinstance(value, int):
            instance._year = value
        else:
            raise ValueError('Year must be an integer')

class Car:
    brand = Brand()
    model = Model()
    year = Year()
    
    def __init__(self, brand, model, year):
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

# Test the Car class
car = Car('BMW', 'M4', 2023)
result = car.count_attributes()
print(result)













# import json
# with open('states.json') as file_state:
#     data = json.load(file_state)
# print(data)