# x = int(input("შეიყვანეთ რიცხვი:"))
# if x > 0:
#     print("dadebiti")
#     x+=10
# elif x == 0:
#     print("ricxvi tolia 0is")
#     x+=2
#     print(x)
# # else:
# #     print("ricxvi uaryofitia")
    
# # print(x)

# # st="ffffg"
# # for i in st:
# #     if i=="g":
# #         st+="georgia"
# #         continue
              
              
# #     print(i, end=" ")
# # else:
# #     print(" no")

# from random import randint
# from time import time

# initial_depth = 300
# speed = 0
# danger_zone=False

# def helper():
#     global initial_depth,speed,danger_zone
#     speed = randint(-1, 1)
#     initial_depth+=speed
#     if initial_depth <= 0:
#         initial_depth = 0
#     print("depth:", initial_depth)
#     if initial_depth>350:
#         danger_zone=True
#     else:
#         danger_zone=False
#     return [danger_zone, speed, initial_depth]


# def submarine():
#     contact = True
#     while contact:
#         start_time=time()
#         danger_zone,speed,initial_depth=helper()

#         while danger_zone:
#             count = time() - start_time
#             print("time:", int(count))
#             danger_zone,speed,initial_depth=helper()
#             if count > 5:
#                 contact=False
#                 break
#     print("program stopped responding...")
# submarine()

# arr = [ 1,2,3,4,5,6,7,8]
# n=len(arr)
# for i in range(n - 1, 0, -1):
#     print(arr[i])


# import bcrypt
# password = b'123456'
# print(password)
# salt = bcrypt.gensalt()
# print(salt)
# hashed = bcrypt.hashpw(password, salt)
# print(hashed)

# help(sum)

# def is_dict_empty(d):
#     return len(d) == 0

# # Example dictionaries
# empty_dict = {}
# non_empty_dict = {'a': 1, 'b': 2}

# # Check if dictionaries are empty
# print("Is empty_dict empty?", is_dict_empty(empty_dict))
# print("Is non_empty_dict empty?", is_dict_empty(non_empty_dict))


from collections import defaultdict
a = 'ertiorisami'
b = defaultdict(str)
for alb in a:
    b[alb] = a.count(alb)
dc = dict(b)

    
print(b)
