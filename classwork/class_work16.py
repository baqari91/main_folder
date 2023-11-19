import csv
class Car:
    discount_rate = 0.8
    all_cars = []

    def __init__(self, name: str, price: float, number=0):

        assert len(name) > 0, "You entered empty string!"
        assert len(name) < 15, "Entered name is too long!"
        assert price > 0, "Price must be Positive number!"

        self.__name = name
        self.price = price
        self.number = number

        Car.all_cars.append(self)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        assert len(value) > 0, "You entered empty string!"
        assert len(value) < 15, "Entered name is too long!"
        
        self.__name = value
        
        
    

    def total_price(self):
        return self.price * self.number

    def calculate_discount(self):
        return self.price * self.discount_rate

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name}, {self.price}, {self.number})"

    @classmethod
    def create_object(cls):
        with open("cars.csv", "r") as file:
            cars_info = list(csv.DictReader(file))

            for car in cars_info:
                Car(
                    name=car["name"],
                    price=float(car["price"]),
                    number=float(car["quantity"])
                )




car1 = Car("BMW1", 3000,3)
car2 = Car("BMW2", 4000,4)
car3 = Car("BMW3", 5000,5)


print (car3.calculate_discount())

class ElectricCar(Car):
    km_per_percent = 3
    def __init__ (self,charged:float, name,price,quantity):
        assert charged > 0,'it must be more than 0%'
        assert charged < 100, "it can't be more than 100% "
        self.charged = charged
        Car.__init__(self,name,price,quantity)
    def kilometers(self):
        return self.charged * self.km_per_percent
   
    @staticmethod
    def moving():
        print('car is moving')
    
    def calculate_discount(self):
        return self.price * 0.7
   
elcar = ElectricCar(80,'BMW', 8000,5)
print(elcar.loop())

# class Parent:
#     def __init__(self,name:str,age:int,income:float):
#         self.__name = name
#         self.age = age
#         self.income = income
#     @property
#     def name(self):
#         return self.__name 
#     @name.setter
#     def name(self,value):
#         if value[0].lower() == 't':
#             self.__name 

# parent1 = Parent('tgiorgi', 20, 4000)
# parent1.name = 'Tlasha'
# print(parent1.name)