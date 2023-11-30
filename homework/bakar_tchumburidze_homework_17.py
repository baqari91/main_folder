#1.დაწერეთ პითონის Car(ატრიბუტები:brand,model,year) კლასი და მახდინეთ ამკლასისთვის __new__ და __init__ მეთოდის გადაფარვა.
class Car:
    def __new__(cls,b,m,y):
        instance = super().__new__(cls)
        print("Creating a new instance of Car")
        print(instance)
        return instance

    def __init__(self, brand, model, year):
        print("Initializing Car instance")
        self.brand = brand
        self.model = model
        self.year = year
        print(self)

# Creating an instance of Car
car = Car("Toyota", "Corolla", 2023)
print(f"Car: {car.brand} {car.model} ({car.year})")


l
#2.შექმენით დეკორატორი, რომელიც დაითვლის და დაგვიბეჭდავს დროს, თუ რა დრო დასჭრიდა ობიექტის მეთოდის შერულებას და დაგვიწერს რა ატრიბუტები აქვს გადმოცემული ობიექტს
#3.შექმენით დეკორატორი, რომელიც დაითვლის და დაგვიბეჭდავს დროს, თუ რა დრო დასჭირდა ობიექტის მეთოდის შესრულებას და დაგვიწერს რა ატრიბუტები აქვს გადმოცემული ობიექს