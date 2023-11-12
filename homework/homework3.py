#ჯეირანი
from random import choice
choice_list = ["rock", "scissors", "paper"]
game_end = False
computer_score=0
human_score=0

while game_end==False:
    computer_choice = choice(choice_list)
    human_choice = input("Enter one of the following: rock / scissors / paper ").lower()
    if human_choice in choice_list:
        if human_choice == computer_choice:
            print("Draw!")
        elif (human_choice == "rock" and computer_choice == "scissors") or (human_choice == "scissors" and computer_choice == "paper") or (human_choice == "paper" and computer_choice == "rock"):
            print("Human Wins!")
            human_score+=1
            print(f"Computer-Human {computer_score}-{human_score}")
        else:
            print("Computer Wins!")
            computer_score+=1
            print(f"Computer-Human {computer_score}-{human_score}")
    if human_score==3 or computer_score==3:
        game_end=True
        if computer_score==3:  
            print("Game end, Winner is: Computer")
        else:
            print("Game end, Winner is: Human")


# გამრავლების ტაბულა      
a=int(input("enter number: "))
for i in range(1,a+1):
    for j in range(1,a+1):
       print(i*j,  end=" ")   
    print()


#საბანკო ანგარიში
stop=False
expense=0 
bank_account=3000

while stop==False:
    a=int(input("Item fee: "))
    if a<=bank_account:
        if a==0:
            stop=True
            print(f"თვენ დახარჯეთ{expense} ლარი და ანგარიშზე დაგრჩათ {bank_account} ლარი")
        bank_account-=a
        print("თქვენ დაგრჩათ:", bank_account, "თანხა")
        expense+=a
    else:
        print("ანგარიშზე არ არის საკმარისი თანხა")


# თუთიყუში
while True:
    user_said=input("enter word: ")
    if user_said.lower() == "quit":
        print("User said whaaat!?")
        break
    print(f"User said whaaat!?\nUser Said {user_said}")

    