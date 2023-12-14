import json
import pickle
import os
import dill


def serialization(obj):
    try:
        with open('data.json', 'w') as file:
            json.dump(obj, file)
            print("Data saved by json")
            return 'data.json'
    except Exception as e:
        os.remove('data.json')
        print('Error saving data by json:', e)
        try:
            with open('data.pickle', 'wb') as file:
                pickle.dump(obj, file)
                print("Data saved by pickle")
                return 'data.pickle'
        except Exception as e:
            print('Error saving data by pickle:', e)
            os.remove('data.pickle')
            try:
                with open('data.dill', 'wb') as file:
                    dill.dump(obj, file)
                    print('Data saved by dill')
                    return 'data.dill'

            except Exception as e :
                print('Error saving data by dill:', e)
                print('Serialization impossible')


def deserialization(file_name):
    if not os.path.exists(file_name):
        print(f'File {file_name} does not exist')
        return None

    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            print('Deserialized data using json:', data)
            return data
    except Exception as e:
        print('Error deserializing with json:', e)
        try:
            with open(file_name, 'rb') as file:
                data = pickle.load(file)
                print('Deserialized data using pickle:', data)
                return data
        except Exception as e:
            print('Error deserializing with pickle:', e)
            try:
                with open(file_name, 'rb') as file:
                    data = dill.load(file)
                    print('Deserialized data using dill:', data)
                    return data
            except Exception as e:
                print('Error deserializing with dill:', e)
                print('Deserialization impossible')


class SimpleObject:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def call_obj(self):
        print(self.name)


obj1 = SimpleObject('class object')
string = 's'
lst = [1, 2, 3]
lambda_func = lambda x: x ** 2

serialization(lambda_func)
print(deserialization('data.dill')(10))
