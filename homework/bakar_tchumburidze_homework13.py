# 1. დაწერე ფუნქცია რომელიც მომხმარებელს ჩააწერინებს ფაილში ინფორმაციას
# Input ფუნქციის დახმარებით, მანამ სანამ მომხმარებელი არ შეიყვანს სიტყვას _ “enough”. input_ ფუნქცია და ციკლი არ უნდა იყოს ფუნქციის შიგნით.
# ციკლში უნდა მოხდეს ფუნქციის გამოძახება, მაშინ თუ ფაილი გაშვებულია შიგნიდა (if __name__ == "__main__")

def add_info(new_info):
    with open('library.txt', 'a') as f:
        f.write(f'{new_info}\n')

cycle_end = True

while cycle_end:
    info = input("enter new info:")
    if info.lower() == "enough":
        cycle_end = False
    else:
        if __name__ == "__main__":
            add_info(info)


# 2. დაწერე ფუნქცია რომელიც input ფუნქციის დახმარებით მომხმარებლისგან მიიღებს საქაღალდის ლოკაციას და შესაქმნელი ფაილის სახელს, 
# შემდეგ მიღებულ ლოკაციაზე შექმნის შესაბამის ფაილს და ამოპრინტავს საქაღალდეში არსებულ ყველა ფაილის სიას.
import os
file_name_from_input = input('enter file name: ') + '.txt'
directory_patch = input('enter directory patch: ') + '/'

def create_file(path, file_name):
    file_patch = path + file_name
    with open(file_patch,'w') as f:
        pass
    print(os.listdir(path))

create_file(directory_patch,file_name_from_input)


# 3. შექმენი ფუნქცია რომელიც input_ით შეყვანილ ტექსტს დაშიფრავს მორზეს ანბანით და ისე შეინახავს ფაილში (2 დავალებაში შექმნილ ფაილში).
input_text = input('enter text: ')
def morse_code(word):

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
    return morse_word

def text_to_morse_code(text,file):
    with open(file, 'a') as f:
        f.write(morse_code(text)+ '\n' )
    
text_to_morse_code(input_text,file_name_from_input)

   


