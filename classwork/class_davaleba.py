import json
import pickle
import os
def a (obj):
    try:

        with open('data.json', 'w') as file:
            json.dump(obj, file)
            print("data saved with json")
    except:
        os.remove('data.json')
        print('can not saved data with json')
        try:
            with open('data.pickle', 'wb') as file:
                pickle.dump(obj, file)
                print("data saved with pickle")
        except:
            print('can not object saved data')
def b (file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            print(data, 'works json')
    except:
        print('Cannot deserialize  with json')
        try:
            with open(file_name, 'rb') as file:
                data = pickle.load(file)
                print(data, 'works pickle')
        except:
            print('Cannot deserialize')
class SimpleObject:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
    def call_obj (self):
        print(self.name)
obj1 = SimpleObject('class object')
string = 's'
integer = 5
boolean = True
lst = [1, 2, 3]

print((obj1))
a(obj1)
# b('data.pickle')