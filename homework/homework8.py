# დავალება 1
li= [1,2,3,4,5,6,7]
result = list(map(lambda arg: arg*10, li))
print(result)

# დავალება 2
names = ["alice", "bob", "claire", "david", "ella", "Ethan", "Fiona", "George", "Hannah", "Isabella"]
result = list(filter(lambda arg: arg[0].isupper(),names))
print(result)

#დავალება 3
li = [-10,-20,-30,10,20,30]
positive_numbers = sum(filter(lambda x: x>0, li))
negative_numbers = sum(filter(lambda x: x<0, li))
print("positive numbers sum:}",positive_numbers)
print("negative numbers sum:}",negative_numbers)

#დავალება 4
user = []
creating=0
while True:
    try:
        while creating<=2:
            if creating==0:
                user.append(input("enter account name: "))
                creating+=1
            elif creating==1:
                user.append(input("enter account password: "))
                creating+=1       
            else:
                user.append(int(input("enter deposit: ")))
                creating+=1
    except:
        print("please enter deposit by numbers")
    if creating==3:
        print("you are registred")
        break
    
while True:
    a = input("enter your account name: ")
    b = input("enter your password: ")
    
    if a==user[0] and b==user[1]:
            print(f"you are logined\nyour ballance is {user[2]}")
            break
    else:
        print("name or password not corecrtly\nplease try again")

