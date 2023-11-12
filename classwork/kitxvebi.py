user=[]
a=input("enter name: ")
b=input("enter password: ")
registration=False
if len(a)>0  and len(b)>=8:
    user.append(a)
    user.append(b)
    registration=True
    print("თქვენ წარმატებით დარეგისტრირდით")
else:
    print("გთხოვთ შეიყვანოთ ინფორმაცია ზუსტად")
if registration==True:
    f_name=input("enter your name: ")
    password=input("enter your password: ")
    if f_name==user[0] and password==user[1]:
        print("თქვენ წარმატებით გაიარე ავტორიზაცია")
    

# # რატომ არ აგრძელებს კოდი მუშაობას



# if len(a)>0  and len(b)>=8:
#         user.append(a)
#         user.append(b)
#         print("თქვენ წარმატებით დარეგისტრირდით")
#         f_name=input("enter your name: ")
#         password=input("enter your password: ")
#         if f_name==user[0] and password==user[1]:
#             print("თქვენ წარმატებით გაიარე ავტორიზაცია")
#             login=True
#         else:
#             print("მომხმარებლის სახელი ან პაროლი არასწორია")
# else:
#     print("გთხოვთ შეიყვანოთ ინფორმაცია ზუსტად")
