# დავალება 1
a=[]
b=[]
c=[]
h=0
while h<=2:
    if h==0:
        a.append(input("Enter your Name: "))
        a.append(input("Enter your Lastname: "))
        a.append(int(input("Enter your Age: ")))
        h+=1
    elif h==1:
        b.append(input("Enter your Name: "))
        b.append(input("Enter your Lastname: "))
        b.append(int(input("Enter your Age: ")))
        h+=1
    else:
        c.append(input("Enter your Name: "))
        c.append(input("Enter your Lastname: "))
        c.append(int(input("Enter your Age: ")))
        h+=1
consumer_info = [a,b,c]
ind=int(input("enter index: "))
if ind == 0:
    print(f"Name: {consumer_info[0][0]}\nLastname: {consumer_info[0][1]}\nAge: {consumer_info[0][2]}")
if ind == 1:
    print(f"Name: {consumer_info[1][0]}\nLastname: {consumer_info[1][1]}\nAge: {consumer_info[1][2]}")
if ind == 2:
    print(f"Name: {consumer_info[2][0]}\nLastname: {consumer_info[2][1]}\nAge: {consumer_info[2][2]}")

# დავალება 2    

user=[]
a=input("enter name: ")
b=input("enter password: ")

if len(a)>0  and len(b)>=8:
    user.append(a)
    user.append(b)
    print("თქვენ წარმატებით დარეგისტრირდით\nშეიყვანეთ მომხმარებლის სახელი და პაროლი")
    f_name=input("enter your name: ")
    password=input("enter your password: ")
    if f_name==user[0] and password==user[1]:
        print("თქვენ წარმატებით გაიარეთ ავტორიზაცია")  
    else:
        print("მომხმარებლის სახელი ან პაროლი არასწორია")
else:
    print("გთხოვთ შეავსოთ ყველა ველი ზუსტად")

# დავალება 3

actors = [
    ["Tom", "Hanks", 1956, "American"],
    ["Meryl", "Streep", 1949, "American"],
    ["Leonardo", "DiCaprio", 1974, "American"],
    ["Jennifer", "Lawrence", 1990, "American"],
    ["Johnny", "Depp", 1963, "American"],
    ["Cate", "Blanchett", 1969, "Australian"],
    ["Daniel", "Day-Lewis", 1957, "British"],
    ["Natalie", "Portman", 1981, "American"],
    ["Denzel", "Washington", 1954, "American"],
    ["Julia", "Roberts", 1967, "American"]
]

a=input("enter actor's name or lastname: ").lower()
found = False
for i in actors:
    f_name,l_name,birth_year,nationality = i
    if a == f_name.lower() or a == l_name.lower() :
        print(f"Actor's Resume:\nFullname: {f_name} {l_name}\nBirth Year: {birth_year}\nNationality: {nationality}")
        found = True
if not found:
    print("actor not found")  
        

