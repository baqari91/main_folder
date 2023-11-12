# lam = lambda x,y:x*y
# print(lam(4,5))

# li = [lambda arg=x: arg**2 for x in range(1,20)]
# for item in li:
#     print(item())

# multiplication = [lambda arg1=x, arg2=y: arg1*arg2 for x in range(1,11) for y in range(1,11)]
# for i, item in enumerate(multiplication):
#     if i%10==0 and i != 0:
#         print()
#     print(item(), end=" ")

# multiplication = [lambda arg1=x, arg2=y: arg1*arg2 for x in range(1,11) for y in range(1,11)]
# i=0
# def mult(func_list):
#     global i
#     if i%10==0 and i != 0: 
#         print()
#     print(func_list[i](), end=" ")
#     if i < len(func_list)-1:
#         i+=1
#         mult(func_list)
# mult(multiplication)


# is_num = lambda text: text.isdigit()
# print(is_num("3"))

# is_greate = lambda arg: True if len(arg) > 5 else False
# print(is_greate(33))




# li = [1,2,3,4,5]

# def test(n):
#     return n+5

# new_li = list(map(test,li))

# print(new_li)

# li = [1,2,3,4,5]
# def test(n):
#     if n % 2==0:
#         return n
#     else:
#         return "is odd"
# new_li = list(map(test,li))
# print(new_li)

from functools import reduce
li = [-4,14,55,222,-3,55]
min = reduce(lambda a,b: a if a<b else b, li)
print(min)
