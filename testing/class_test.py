
# class Human:
#     height = 170
#     weight = 70
#     all_peaple = []
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#         #print('init')
#         self.all_peaple.append(self)
#     def __repr__(self):
#         return (f'Human(name:{self.name},age:{self.age})')
#     def sleep(self):
#         print(f'{self.name} is sleeping')
    
#     @staticmethod
#     def check_type(x):
#         return type(x)
#     @classmethod
#     def peaple_by_age(cls,name):
#         return [peaple for peaple in cls.all_peaple if peaple.name == name ]

# class Georgian(Human):
#     location = 'Kavkasia'

#     def tamadoba(self):
#         print('Sadgegrdzelo')


# geo = Georgian('Dato',19)
# geo.tamadoba()
# geo1 = Georgian('avto',10)
# geo1 = Georgian('avto', 11)
# print(geo1,'h')
# print(geo1.name)
# print (Human.peaple_by_age('avto'))
# print(Human.all_peaple)




   

# class Georgian():
#     all_peaple = []
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#         self.all_peaple.append(self)
#     def __repr__(self):
#         return (f'Human(name:{self.name},age:{self.age})')

    
#     @classmethod
#     def peaple_by_age(cls,name):
#         return [peaple for peaple in cls.all_peaple if peaple.name == name ]


# geo1 = Georgian('Dato',19)
# geo1 = Georgian('avto',10)
# geo1 = Georgian('avto', 11)
# print(geo1)
# print(Georgian.all_peaple)


class Georgian():
    all_people = []
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.all_people.append(self)
        
    def __repr__(self):
        return f'Human(name: {self.name}, age: {self.age})'

    @classmethod
    def get_or_create_instance(cls, name, age):
        for person in cls.all_people:
            if person.name == name:
                print(f"Instance with name '{name}' already exists!")
                return person
        return cls(name, age)

# Example usage
geo1 = Georgian('Dato', 19)  # Creates normally
geo1 = Georgian.get_or_create_instance('Dato', 20)  # Doesn't recreate, uses the existing 'Dato' instance
geo1 = Georgian.get_or_create_instance('Avto', 21)  # Creates a new instance with 'Avto'

print(Georgian.all_people)
