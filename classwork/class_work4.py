
# name=input("enter your name: ")
# def sayhello(user_name):
#     print(f"hello {user_name}")
# sayhello(name)


# def numbers():
#     a=input("enter number: ")
#     b=input("enter number: ")
#     c=input("enter number: ")
#     return (max(a,b,c))
# print(numbers())

# a = [1,2,3,4]
# def num_sum(info):
#     c = 0
#     for i in info:
#         c+=i
#     print(c)
#     return c
# num_sum(a)
    
# def rev():
#     a=input("enter string: ")
#     result = a[::-1]
#     print(result)
# rev()

# a = [1,1,2,4,4,6,73,5,6,7,2,4,1]

# def abc(b):
#     result=[]
#     for i in b:
#         if i not in result:
#             result.append(i)
#     return result
# print(abc(a))

# def check(num):
#     for i in range(2,num//2+2):
#         if num % i == 0:
#             print("num is not simple")
#             break
#     else:
#         print("num is simple")
        
# check(27)

# a = [2,4,7,8,4,9,1]

# def odd(info):
#     for i in info:
#         if i%2==0:
#             print(i)
# odd(a)

# def run_code():
#     code=input("enter code: ")
#     exec(code)
# run_code()

# def wiki():
#     theme=input("enter text: ")
#     return f"https://en.wikipedia.org/wiki/{theme}"
# print(wiki())

# from random import randint
# def guest_number():
#     number=randint(1,300)
#     i = 0
#     while True:
#         num=int(input("enter number: "))
#         i+=1
#         if num == number:
#             print("congratulations")
#             break
#         else:
#             if num>number:
#                 print("ჩემი ციფრი ნაკლებია ")
#             else:
#                 print("ჩემი ციფრი მეტია")
#     print(f"tries: {i}")
# guest_number()
    




# import random

# words = ["tomato", "bird", "human"]
# word = random.choice(words)
# guess_word = []
# health = len(word) + 5
# for i, symbol in enumerate(word):
#     if i == 0:
#         guess_word.append(symbol)
#     elif symbol == word[0]:
#         guess_word.append(symbol)
#     else:
#         guess_word.append("-")
# while health > 0:
#     for symbol in guess_word:
#         print(symbol, end=" ")
#     print()
#     guess_symbol = input("Enter symbol: ").lower()
#     if (guess_symbol in word) and (guess_symbol not in guess_word):
#         for i, symbol in enumerate(word):
#             if symbol == guess_symbol:
#                 guess_word[i] = symbol
#     else:
#         health -= 1
#         print(health)
#     if "-" not in guess_word:
#         print("You Win!")
#         print(guess_word)
#         break
        

