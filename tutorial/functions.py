# # კალკულატორი
# x=int(input("ციფრი 1:"))
# y=int(input("ციფრი 2:"))

# def calc (a,b =1): #მეორე პარამეტრად მინიჭებული აქვს დეფაულთ მნიშვნელობა იმ შემთვევისთვის თუ არგუმენტი მიწოდებული არ არის. არ არის რეკომენდირებული პირველს მივანიჭოთ დეფაულთი და მეორეს და შემდეგებს არ.
#     jami=a+b
#     sxvaoba=a-b
#     gayofa=a/b
#     namravli=a*b
#     return jami,sxvaoba,gayofa,namravli

# print(calc (x,y))  # არგუმენტი პარამეტრს მიეწოდება თანმიმდევრობით. თუ გვინდა რომ მივანიჭოთ კონკრეტული არგუმენტი, კონკრეტულ პარამეტრს მაშინ უნდა ჩავწეროთ მსგავსად  def func(a=birtday, fname="ani, პარამეტრის-სახელი=არგუმენტს")                     

#ასაკის გამოთვლა
# Bday=int(input("დაბადების წელი"))
# def age (year,birtday):
#     return("თქვენი ასაკი არის"+str(year-birtday))
# print(age(2023,Bday))

# # კუბში აყვანა
# def cube(a):
#     x=a**3
#     return x
# input=int(input("ციფრი"))
# print(cube(input))

# #ფუნქცია რომელიც იძახებს სხვა ფუნქციებს
# def age (year,birthday):
#     return("your age is: "+str(year-birthday))
# def hello(name):
#     return("Hello "+name+", ")
# def main ():
#     y=int(input("Enter year: "))
#     b=int(input("enter your birthdate: "))
#     n=input("enter your name: ")
#     print(hello(n)+age(y,b))
# main ()

# #ფუნქციის სპეციფიური პარატმეტრები.
# def test1 (*args):         # განუსაზღვრელი რაოდენობის არგუმენტების მიღება, 
#     return args       #!!!!!
# def test2 (**kwargs):      # განუსაზღვრელი რაოდნეობის არგუმენტების მიღება პარამეტრის სახელწოდებით მაგ: პარამეტრი=არგუმენტს
#     return kwargs     #!!!!!    
# print(test2(x=7,y=2))

# # შიდა ფუნქციაზე წვდომა გარედან
# def func1 (x):
#     def func2(y):
#         print(x+y)
#     return func2

# new =func1(10)         
# new (50)   # მიეწოდება პარამეტრად func2-ს

# # lambda ფუნქცია. ანონიმური ფუნქცია სახელის გარეშე
# c = lambda a,b:a+b   # ანონიმური ფუნქცია მინიჭებული ცვლადზე, პარამეტრები გადაეცემა ცვლადის გამოძახებით
# print(c(4,5))

# print((lambda a,b:a+b)(4,4)) # ადგილობრივად გამოყენება ცვლადის შექმნის გარეშე, პარამეტრი გადაეცემა ადგილობრივად

# რეკურსიული ფუნქციები მაგალითი
# def rec(n):     #ადის უმაღლეს მნიშვნელობაბმდე და შემდეგ უკან ჩამოდის
#     if n<4:
#         print(n)
#         rec(n+1)
#         print(n)
# rec(1)