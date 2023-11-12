# a = []

# while len(a)<5:
#     a.append(input("enter info: "))
# print(a)

# a = ["red","black","green","yellow"]
# b, * c,d=a
# print(b)
# print(c)
# print(d)


# a = ["red","black","green","yellow"]
# b=input("enter name of item: ")
# if b in a:
#     a.remove(b)
# print(a)

# a = ["red","black","green","yellow"]
# for index,i in enumerate(a):
#     print(index,i)


# a=[1,2,3]
# b=[4,5,6]
# print(a*5)

# a=[1,2,3]
# b=[4,5,6]
# a.extend(b)
# print(a)

# a=[1,2,3]
# b=a[::-1]
# print(b)

# a=[1,2,3]
# a.reverse()
# print(a)

# from random import randint
# a = []
# b = int(input("enter 1st number: "))
# c = int(input("enter 2nd number: "))
# while len(a)<=4:
#     a.append(randint(b,c))
# print(a)

# import random 
# a = []
# b = int(input("enter 1st number: "))
# c = int(input("enter 2nd number: "))
# while len(a)<=4:
#     a.append(random.randint(a,b))
# print(a)

# a = [1,2,3,1,5,7,7]
# a.insert(2,True)
# print(a)

map = [[1,2,3],
       [4,5,6],
       [7,8,9]
       ]

while True:
    player1 = int(input("enter number 1/9 :"))
    for row in map:
        for index, item in enumerate(row):
            if player1 == item:
                row.pop(index)
                row.insert(index, "X")
                break      
    print(map[0])
    print(map[1])
    print(map[2])
    if (map[0][0]=="X" and map[0][1]=="X" and map [0][2]=="X") or (map[1][0]=="X" and map[1][1]=="X" and map [1][2]=="X") or (map[2][0]=="X" and map[2][1]=="X" and map [2][2]=="X") or (map[0][0]=="X" and map[1][0]=="X" and map [2][0]=="X")or (map[0][1]=="X" and map[1][1]=="X" and map [2][1]=="X") or (map[0][2]=="X" and map[1][2]=="X" and map [2][2]=="X")or (map[0][0]=="X" and map[1][1]=="X" and map [2][2]=="X")or (map[0][2]=="X" and map[1][1]=="X" and map [2][0]=="X"):
        print("win X")
        break

    player2 = int(input("enter number 1/9 :"))
    for row in map:
        for index, item in enumerate(row):
            if player2 == item:
                row.pop(index)
                row.insert(index, "O")
                break  
    print(map[0])
    print(map[1])
    print(map[2])
    if (map[0][0]=="O" and map[0][1]=="O" and map [0][2]=="O") or (map[1][0]=="O" and map[1][1]=="O" and map [1][2]=="O") or (map[2][0]=="O" and map[2][1]=="O" and map [2][2]=="O") or (map[0][0]=="O" and map[1][0]=="O" and map [2][0]=="O")or (map[0][1]=="O" and map[1][1]=="O" and map [2][1]=="O") or (map[0][2]=="O" and map[1][2]=="O" and map [2][2]=="O")or (map[0][0]=="O" and map[1][1]=="O" and map [2][2]=="O")or (map[0][2]=="O" and map[1][1]=="O" and map [2][0]=="O"):
        print("win O")
        break

 
    
            

