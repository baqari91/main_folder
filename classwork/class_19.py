import pickle
import json
import dill
# string = 'hello'
# data = pickle.dumps(string)
# print(data)
# data1 = pickle.loads(data)
# print(data1)

# costumers = {'costumer': ['name','sandro'], 'gender': ['male', True]}
# data_dic = pickle.dumps(costumers)
# print(data_dic)
# data_dic1 = pickle.loads(data_dic)
# print(data_dic1)

# tpl = (1, 2, 3)
# data_tpl = pickle.dumps(tpl)
# print(pickle.loads(data_tpl))
#
# js_tpl = json.dumps(tpl)
# print(js_tpl)

# class SimpleObject:
#     def __init__(self, name):
#         self.name = name
#     def __repr__(self):
#         return self.name
#     def call_obj (self):
#         print(self.name)
# obj1 = SimpleObject('saxeli')
# with open('pickle_new.pickle', 'wb') as file:
#     pickle.dump(obj1, file)
#
# # with open('pickle_new.json', 'w') as file:
# #     pickle.dump(obj1, file)
# with open('pickle_new.pickle', 'r') as file:
#     data = pickle.load (file)
# print(data)

# num_in_pow = lambda x:x**2
# pow_pick = dill.dumps(num_in_pow)
# print(dill.loads(pow_pick)(4))

import pyscreenshot as screen
# image = screen.grab()
# image.save('1st_img.png')
image = screen.grab(bbox=(30,30,300,600))
image.save('2st_img.png')

