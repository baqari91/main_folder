
from random import randint
from random import choice
computer_positions = [
    [["Maverick",[3]],["Gunner",[8,9]],["Matilda",[13,14,15]]],
    [["Maverick",[4]],["Gunner",[10,11]],["Matilda",[16,17,18]]],
    [["Maverick",[5]],["Gunner",[12,13]],["Matilda",[18,19,20]]]
    ]
game_playing=True
player_destroyed_ship=0
computer_destroyed_ship=0
computer = choice(computer_positions)
player = []
player_creating = 0
generated_numbers = []
for i in computer:
    computer_ship_names,computer_ship_positions=i
    if len(computer_ship_positions)==1:
        computer_smal_ship_position=computer_ship_positions[0] 
        computer_smal_ship_name=computer_ship_names    
    elif len(computer_ship_positions)==2:
        computer_med_ship_position_1,computer_med_ship_position_2=computer_ship_positions
        computer_med_ship_name=computer_ship_names  
    else:
        computer_big_ship_position_1,computer_big_ship_position_2,computer_big_ship_position_3=computer_ship_positions
        computer_big_ship_name=computer_ship_names  

while player_creating<=2:
    if player_creating==0:
        player_smal_ship_name = input("Ship Name: ")
        player_smal_ship_position = int(input("პოზიცია: "))
        player.append(list([player_smal_ship_position]))
        player_creating+=1
    elif player_creating==1:
        player_med_ship_name = input("Medium Ship Name: ")
        start_position_med=int(input("მეორე გემის პირველი უჯრის პოზიცია, დაემატება მომდევნო რიცხვი: "))
        player.append(list(range(start_position_med,start_position_med+2)))
        player_creating+=1
    else:
        player_big_ship_name = input("Big Ship Name: ")
        start_position_big = int(input("მესამე გემის პირველი უჯრის პოზიცია, დაემატება მომდევნო 2 რიცხვი: "))
        player.append(list(range(start_position_big,start_position_big+3)))
        player_creating+=1
player_smal_ship_position = player[0][0]
player_med_ship_position_1,player_med_ship_position_2 = player[1]
player_big_ship_position_1,player_big_ship_position_2,player_big_ship_position_3 = player[2]

while game_playing:
    computer_shoot = randint(1,20)
    if computer_shoot in generated_numbers:
        continue
    generated_numbers.append(computer_shoot)
    print("კომპიუტერის სროლა: ",computer_shoot)
    if computer_shoot == player_smal_ship_position:
        player_smal_ship_position = "x"
        print(f"ჩაიძირა გემი სახელად:{player_smal_ship_name} ")
        computer_destroyed_ship+=1
    if computer_shoot == player_med_ship_position_1:
        print(f"განადგრუდა გემ: {player_med_ship_name}-ის პოზიცია: {player_med_ship_position_1}")
        player_med_ship_position_1 = "x"
        print([[player_smal_ship_position],[player_med_ship_position_1,player_med_ship_position_2],[player_big_ship_position_1,player_big_ship_position_2,player_big_ship_position_3]])
        if player_med_ship_position_2 == "x":
            print(f"ჩაიძირა გემი სახელად:{player_med_ship_name} ")
            computer_destroyed_ship+=1
    if computer_shoot == player_med_ship_position_2:
        print(f"განადგრუდა გემ: {player_med_ship_name}-ის პოზიცია: {player_med_ship_position_2}")
        player_med_ship_position_2 = "x"
        print([[player_smal_ship_position],[player_med_ship_position_1,player_med_ship_position_2],[player_big_ship_position_1,player_big_ship_position_2,player_big_ship_position_3]])
        
        if player_med_ship_position_1 == "x":
            print(f"ჩაიძირა გემი სახელად:{player_med_ship_name} ")
            computer_destroyed_ship+=1
    if computer_shoot == player_big_ship_position_1:
        print(f"განადგრუდა გემ: {player_big_ship_name}-ის პოზიცია: {player_big_ship_position_1}")
        player_big_ship_position_1 = "x"
        print([[player_smal_ship_position],[player_med_ship_position_1,player_med_ship_position_2],[player_big_ship_position_1,player_big_ship_position_2,player_big_ship_position_3]])
        
        if player_big_ship_position_2 == "x" and player_big_ship_position_3 == "x":
            print(f"ჩაიძირა გემი სახელად:{player_big_ship_name} ")
            computer_destroyed_ship+=1
    if computer_shoot == player_big_ship_position_2:
        print(f"განადგრუდა გემ: {player_big_ship_name}-ის პოზიცია: {player_big_ship_position_2}")
        player_big_ship_position_2 = "x"
        print([[player_smal_ship_position],[player_med_ship_position_1,player_med_ship_position_2],[player_big_ship_position_1,player_big_ship_position_2,player_big_ship_position_3]])
        
        if player_big_ship_position_1 == "x" and player_big_ship_position_3 == "x":
            print(f"ჩაიძირა გემი სახელად:{player_big_ship_name} ")
            computer_destroyed_ship+=1
    if computer_shoot == player_big_ship_position_3:
        print(f"განადგრუდა გემ: {player_big_ship_name}-ის პოზიცია: {player_big_ship_position_3}")
        player_big_ship_position_3 = "x"
        print([[player_smal_ship_position],[player_med_ship_position_1,player_med_ship_position_2],[player_big_ship_position_1,player_big_ship_position_2,player_big_ship_position_3]])
        
        if player_big_ship_position_1 == "x" and player_big_ship_position_3 == "x":
            print(f"ჩაიძირა გემი სახელად:{player_big_ship_name} ")
            computer_destroyed_ship+=1

    player_shoot = int(input("ესროლეთ პოზიციას 1-იდან 20-მდე: "))
    if player_shoot == computer_smal_ship_position:
        computer_smal_ship_position = "x"
        print(f"ჩაიძირა გემი სახელად:{computer_smal_ship_name} ")
        player_destroyed_ship+=1
    if player_shoot == computer_med_ship_position_1:
        print(f"განადგრუდა გემ: {computer_med_ship_name}-ის პოზიცია: {computer_med_ship_position_1}")
        computer_med_ship_position_1 = "x"
        if computer_med_ship_position_2 == "x":
            print(f"ჩაიძირა გემი სახელად:{computer_med_ship_name} ")
            player_destroyed_ship+=1
    if player_shoot == computer_med_ship_position_2:
        print(f"განადგრუდა გემ: {computer_med_ship_name}-ის პოზიცია: {computer_med_ship_position_2}")
        computer_med_ship_position_2 = "x"
        if computer_med_ship_position_1 == "x":
            print(f"ჩაიძირა გემი სახელად:{computer_med_ship_name} ")
            player_destroyed_ship+=1
    if player_shoot == computer_big_ship_position_1:
        print(f"განადგრუდა გემ: {computer_big_ship_name}-ის პოზიცია: {computer_big_ship_position_1}")
        computer_big_ship_position_1 = "x"
        if computer_big_ship_position_2 == "x" and computer_big_ship_position_3 == "x":
            print(f"ჩაიძირა გემი სახელად:{computer_big_ship_name} ")
            player_destroyed_ship+=1
    if player_shoot == computer_big_ship_position_2:
        print(f"განადგრუდა გემ: {computer_big_ship_name}-ის პოზიცია: {computer_big_ship_position_2}")
        computer_big_ship_position_2 = "x"
        if computer_big_ship_position_1 == "x" and computer_big_ship_position_3 == "x":
            print(f"ჩაიძირა გემი სახელად:{computer_big_ship_name} ")
            player_destroyed_ship+=1
    if player_shoot == computer_big_ship_position_3:
        print(f"განადგრუდა გემ: {computer_big_ship_name}-ის პოზიცია: {computer_big_ship_position_3}")
        computer_big_ship_position_3 = "x"
        if computer_big_ship_position_1 == "x" and computer_big_ship_position_3 == "x":
            print(f"ჩაიძირა გემი სახელად:{computer_big_ship_name} ")
            player_destroyed_ship+=1

    if player_destroyed_ship==3:
        game_playing=False
        (print("გილოცავ გაიმარჯვე"))
    if computer_destroyed_ship==3:
        game_playing=False
        (print("გაიმარჯვა კომპიუტერმა"))







