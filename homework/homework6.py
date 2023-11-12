# # დავალება 1
def tripled():  
    info=input("enter info: ")
    print(info*3)     
tripled()

# დავალება 2
def moon_gravity():
    weight=int(input("enter your weight by kg: "))
    moon_weight=weight/6
    print("your weight on the moon will be:", moon_weight)
moon_gravity()

# დავალება 3
   
def calculator():
    gamosaxuleba=input("ჩაწერეთ რიცხვითი გამოსახულება (მაგ: 5 + 3): ")
    num1,moqmedeba,num2=gamosaxuleba.split()
    if num1.isdigit() and num2.isdigit():
        num1,num2=int(num1),int(num2)
        if moqmedeba=="+":
            result=num1+num2
        elif moqmedeba=="-":
            result=num1-num2
        elif moqmedeba=="*":
            result=num1*num2
        elif moqmedeba=="/":
            if num2==0:
                return ("ნულზე გაყოფა არ შეიძლება")
            else:
                result=num1/num2
        elif moqmedeba=="^":
            result=num1**num2
        else:
            return ("მოქმედებაში უნდა შეიყვანოთ მხოლოდ ეს სიმბოლოები: +,-,*,/,^.")
        return result
    else:
        return ("პირველი და ბოლო ველი უნდა იყოს შევსებული ციფრებით")
print(calculator())

# მორზას ანბანი
def morse_code():
    word=input("enter word: ")
    morse_word=""
    morse_code = [
         [ ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", 
    "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
    "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----." ]
    ]
    for morse in morse_code:
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,n0,n1,n2,n3,n4,n5,n6,n7,n8,n9 = morse
    for symbol in word:
        if symbol.lower() == "a":
            morse_word+=a
        elif symbol.lower() == "b":
            morse_word+=b
        elif symbol.lower() == "c":
            morse_word+=c
        elif symbol.lower() == "d":
            morse_word+=d
        elif symbol.lower() == "e":
            morse_word+=e
        elif symbol.lower() == "f":
            morse_word+=f
        elif symbol.lower() == "g":
            morse_word+=g
        elif symbol.lower() == "h":
            morse_word+=h
        elif symbol.lower() == "i":
            morse_word+=i
        elif symbol.lower() == "j":
            morse_word+=j
        elif symbol.lower() == "k":
            morse_word+=k
        elif symbol.lower() == "l":
            morse_word+=l
        elif symbol.lower() == "m":
            morse_word+=m
        elif symbol.lower() == "n":
            morse_word+=n
        elif symbol.lower() == "o":
            morse_word+=o
        elif symbol.lower() == "p":
            morse_word+=p
        elif symbol.lower() == "q":
            morse_word+=q
        elif symbol.lower() == "r":
            morse_word+=r
        elif symbol.lower() == "s":
            morse_word+=s
        elif symbol.lower() == "t":
            morse_word+=t
        elif symbol.lower() == "u":
            morse_word+=u
        elif symbol.lower() == "v":
            morse_word+=v
        elif symbol.lower() == "w":
            morse_word+=w
        elif symbol.lower() == "x":
            morse_word+=x
        elif symbol.lower() == "y":
            morse_word+=y
        elif symbol.lower() == "z":
            morse_word+=z
        elif symbol.lower() == "0":
            morse_word+=n0
        elif symbol.lower() == "1":
            morse_word+=n1
        elif symbol.lower() == "2":
            morse_word+=n2
        elif symbol.lower() == "3":
            morse_word+=n3
        elif symbol.lower() == "4":
            morse_word+=n4
        elif symbol.lower() == "5":
            morse_word+=n5
        elif symbol.lower() == "6":
            morse_word+=n6
        elif symbol.lower() == "7":
            morse_word+=n7
        elif symbol.lower() == "8":
            morse_word+=n8
        elif symbol.lower() == "9":
            morse_word+=n9
        elif symbol.lower() == " ":
            morse_word+=" "
        else:
            print("მითითებული სიმბოლო არ არსებობს")
            continue
    print(morse_word)
    
morse_code()    

# X da O დამატებულია მოგების შემთხვევაში თამაშის დამთავრება
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
 