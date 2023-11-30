class VerboseDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f"Accessing attribute '{self.name}'")
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        print(f"Setting attribute '{self.name}' to '{value}'")
        instance.__dict__[self.name] = value

class MyClass:
    attribute = VerboseDescriptor("attribute")

# Usage
obj = MyClass()
obj.attribute = '66'  # This will trigger the __set__ method of the descriptor
print(obj.attribute)  # This will trigger the __get__ method of the descriptor
