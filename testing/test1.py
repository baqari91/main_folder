# my_dict4 = {'a':1,'b':2,'c':3}
# def dict_to_list(dict4):
#     created_list = dict4.items()
    
#     return created_list
# print(dict_to_list(my_dict4))

# my_dict4 = {'a':1,'b':2,'c':3}
# def dict_to_list(dict4):
#     created_list = []
#     for k,v in dict4.items():
#         created_list.append(k)
#         created_list.append(v)
#     return created_list
# print(dict_to_list(my_dict4))


# from collections import defaultdict
# order_dict = defaultdict(int)
# order_dict = order_dict['ee']
# order_dict = order_dict['eee']
#
# print(order_dict)

li = ['1',1,'3','4']
s = True
d = repr(s)
test = repr(li)
print(type(test))
print(type(s))
print(s)
print(d)

if d == 1:
    print('yes')