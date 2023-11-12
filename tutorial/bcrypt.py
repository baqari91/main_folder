# tup = tuple ([1,2,3,4,5,6,"erti",True])
# a = [1,2,3,4,5]
# aa,b,c,d,e = a
# print(c)

# a = ('a',"b",'s','f')
# print(" ".join(a))




# s = {1,2,3}
# a = {3,4,5}

# print(s.difference(a))

# import bcrypt
# password = b'qwert'
# print(password)
# salt = bcrypt.gensalt()
# print(salt)
# hashed = bcrypt.hashpw(password,salt)
# print(hashed)
import bcrypt


f_name = input("enter your name: ")
password = input("enter your password: ") 
li = []
def user_info(f_n,passw,user): 
    hashed_pass = bcrypt.hashpw(passw.encode('utf-8'), bcrypt.gensalt())
    user.append((f_n,hashed_pass))
    return user

user_info(f_name,password,li)
print(li)
