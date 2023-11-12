# # # 1
# # my_dict = {'first': 'value1',
# #            'second': 'value2'
# #            }
# # #key-ების წამოღება
# # # for x in my_dict:
# # #     print(x)
# # # value-ების წამოღება
# # for x in my_dict:
# # #     print(my_dict[x])
# # for x in my_dict.values():
# #     print(x)
# # for x in my_dict.keys():
# #     print(x)
# # #წყვილის წამოღება
# # for k,v in my_dict.items():
# #     print(k,v)
# # print(my_dict.items())

# dict_first = {
#     'name':'saxeli'
# }
# dict_first['age'] = '18 year'
# print(dict_first)
# dict_second={
#     'sport': 'footbal'
# }
# dict_first.update(dict_second)
# print(dict_first)
# dict_first.update({1:14})
# print(dict_first)

# def is_key_in_dict():
#     if 'name' in dict_first:
#         print(True)
#     else:
#         print(False)
# is_key_in_dict()


# dict_first = {'num': 15,'num2': 21}
# jami = 0
# for value in dict_first.values():
#     jami+=value
# print(jami)
# print(sum(dict_first.values()))

# dict_first = {'num': 15,'num2': 21}

# def del_element(k,d):
#     if k in d:
#         del d[k]
#         print(d)
#     else:
#         print("this key does't exist")
# del_element('num',dict_first)

# keys = ['one','two','three','four','five',33,66]
# values = [1,2,3,4,5,33,66]
# my_dict = dict(zip(keys,values))

# print(max(my_dict.values()))
# print(min(my_dict.values()))


# from collections import defaultdict

# a = list(range(1,16))
# def create_dict(dict3):
#     my_dict3 = defaultdict(list)
#     for i in dict3:
#         my_dict3[i].append(i**2)
#     return my_dict3
# print(create_dict(a))

# my_dict = {}
# for i in range(1,16):
#     my_dict[i] = i**2
# print(my_dict)

# keys = ['first', 'second', 'third', 'fourth', 'fifth']
# values = [3, 4, 6, 5, 2]
# my_dict = dict(zip(keys, values))

# mult = 1
# for i in my_dict.values():
#     mult *= i

# print(mult)
# print(my_dict)

from collections import defaultdict

fruits = ['apple','banana','avocado','brocoll','orange']
my_dict = defaultdict(list)
for word in fruits:
    my_dict[word[0]].append(word)
print(my_dict)