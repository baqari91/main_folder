# class Human: 
#     height = 180
#     weigh = 70
#     def __init__(self,name):
#         self.name = name
#     def sleep (self):
#         print('human is sleeping')

# human1 = Human('giorgi')
# print(human1.name)
# human1.age = 24
# print(human1.age)
# human1.name = 'lasha'
# print(human1.name)

# class Georgian(Human):
#     location = 'caucasian'

#     def tamada(self):
#         print('gaumarjos')

# geo = Georgian('baqar')
# print(geo.tamada())




# class Parent:
#     password = 'text'
#     def __init__(self,lastname):
#         self.lastname = lastname

# class Parent_2:
#     def __init__(self, language):
#         self.language = language

# class Child(Parent,Parent_2):
#     def __init__(self, name, lastname, language):
#         Parent.__init__(self, lastname)
#         Parent_2.__init__(self, language)
#         # super().__init__(lastname)
#         self.name = name


# child1 = Child('ana','mgebrishvili','georgian')
# child1.password = 'text2'
# print(child1.password)
# print(child1.__class__.password)
# print(child1.language)
# print(child1.name)

# class Car:
#     model = 'mercedes'
#     _lanch_year = '2013'
#     __hores_power = '320'

# car1 = Car()
# print(dir(car1))
# print(car1.model)
# car1._lanch_year = 2222
# print(car1._lanch_year)
# car1._Car__hores_power = 2
# print(car1._Car__hores_power)

from abc import abstractmethod, ABC
class Dog(ABC):
    @abstractmethod
    def bark(self):
        pass
class Dog_2(Dog):
    pass

dog1 = Dog_2()
dog1.bark()