# სიმბოლოების დათვლა
inf = input("enter text: ")
digit=0
alpha=0
other=0
for i in inf:
    a = i.isalpha()
    b = i.isdigit()
    if a:
        alpha+=1
    elif b:
        digit+=1
    else:
        other+=1
print(f"digit symbols: {digit}\nalpha symbos: {alpha}\nother symbols: {other}")

# მეორე დავალება
text_1 = input("enter text: ")
text_2 = input("enter text: ")  
created_text = f"{text_1[0]}{text_2[-1]}{text_1[1]}{text_2[-2]}"
print(created_text)

# მესამე დავალება
inf=input("enter text: ")
inf_count=0
inf_1=input("enter text: ")
inf_1_count=0
for i in inf:
    a=i in inf_1
    if a:
        inf_count+=1
for i in inf_1:
    a=i in inf
    if a:
        inf_1_count+=1
if len(inf)==inf_count and len(inf_1)==inf_1_count:
    print("Strings are balanced!")
else:
    print("Strings are not balanced!")



     
