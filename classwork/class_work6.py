# numbers = [5, 7, 8, 5, 4]
# def histogram(sia):
#     for num in sia:
#         print("*" * num)
# histogram(numbers)

# num = [13,5,23,86,3,5,45,1]
# def find_max(s):
#     max_num = s[0]
#     for i in s:
#         if max<i:
#             max_num = i
#     print(max_num)
# find_max(num)

# li = ["erti", "ori", "sami", "otxi", "Xutiii"]
# def sia(a):
#     max_word=a[0]
#     for word in a:
#         if len(max_word)<len(word):
#             max_word = word
#     print(max_word)
# sia(li)

# a = 5
# def func():
#     global b
#     b = 6
#     print(a)
# func()
# print(b)

# li = [2,4,7,8]
# def mult(a,b,c):
#     print(a*b*c)
# mult(*li)

# def looper(num):
#     print("hi")
#     num-=1
#     if num > 0:
#         looper(num)
# looper(5)

# lst = [1,2,3,4,5]
# i = 0
# def for_loop():
#     global lst,i
#     max_i=len(lst)
#     if max_i > 0:
#         if i<max_i:
#             print(lst[i])
#             i+=1
#             for_loop()
# for_loop()



# from random import randint
# from time import time

# initial_depth = 300
# speed = 0
# danger_zone=False

# def helper():
#     global initial_depth,speed,danger_zone
#     speed = randint(-1, 1)
#     initial_depth+=speed
#     if initial_depth < 0:
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

# a=16
# def func():
#     a = 8
#     def fun1():
        
        
#         print(a)
#     print(a)
#     fun1()
# func()