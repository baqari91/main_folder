# 1 შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე სიას, თუმცა უნიკალური ელემენტებით (გამოიყენე set მონაცემთა ტიპი).
lis = [1,1,2,2,3,3]
def unique_list(li):
    li_to_set = set(li)
    unique_list = list(li_to_set)
    return unique_list
print(unique_list(lis))



# 2 შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე set ტიპის მონაცემს უნიკალური ელემენტებით, რომლის შეცვლაც შეუძლებელი იქნება (გამოიყენე frozenset).
def immutable_set(li):
    frozen_set = frozenset(li)
    return frozen_set
print(type(immutable_set(lis)))


# 3 შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს tuple ტიპის მონაცემად და დააბრუნებს შედეგს.
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
def set_to_tuple(set_1,set_2):
    new_set = tuple(set_1.union(set_2))
    return new_set
print(set_to_tuple(a,b))

# 4 შექმენი ფუნქცია რომელიც მიიღებს მომხმარებლის სახელს და პაროლს, ასევე სიის სახელს. პაროლს გაუკეთებს ჰეშირებას და მონაცემს შეინახავს tuple ტიპის
# მონაცემად გადაცემულ სიაში. შედეგი უნდა დააბრუნოს [("user1", "pass1")]

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

