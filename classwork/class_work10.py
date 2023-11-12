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

dict_first = {'num': 15,'num2': 21}

def del_element(k,d):
    if k in d:
        del d[k]
        print(d)
    else:
        print("this key does't exist")
del_element('num',dict_first)