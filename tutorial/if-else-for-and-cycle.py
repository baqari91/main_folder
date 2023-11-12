# x=int(input("შეიყვანეთ რიცხვი:"))
# if x>0:
#     print("რიცხვი დადებითია")
# elif x<0:
#     print("რიცხვი უარყოფითია")
# else:
#     print('რიცხვი ტოლია 0-ის')


     # ციკლის ოპერატორები
#while ცილკი

i=0
while i<10:
    print(i)
    i+=1 # იგივე რაც i=i+1 ( გაიზარდოს ერთით)
jami=0
n=0
while n<=10:
    jami+=n
    n+=1 # გაიზარდოს ერთით
    print(jami)
# for ციკლი

for i1 in range(0,10,2): #range(start,end,step)
    print(i1 ) 
for i2 in "hello, Georgia ":
    print (i2, end="")  # end="" დაბოლოება როგორი იყოს, პრინტის ფუნქცია

# N1
# for i in range(End)
#     ,,,
# N2
# for i in range(star, end)
#     ...
# N3
# for i in range(star, end, step)
#     ...

# for ციკლის დამატებითი ოპერატორები
for i3 in "gamarjoba":
    if i3=="r":
        continue # გამოტოვე რაც იპოვე
    elif i3=="j":
        break # გააჩერე როცა იპოვი
    print(i3,end="")
else:
    print("ციკლმა ვერ აღმოაჩინა ვერაფერი") # else ოპერატორი ასევე შესაცლებელია for ციკლთან გამოყენება