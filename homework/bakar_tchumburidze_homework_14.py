#დავალება
#ლექსიკონების დახმარებით შექმენი პითონში პროგრამა, რომელიც წარგიდგენს რესტორნის მენიუს. მიიღებს შეკვეთას.
# შექმნის ფაილს და ჩაწერს შეკვეთასა და მის ღირებულებას. პროგრამა გადააქციე exe ფაილად და დაუყენე რესტორნის სურათი.
import os
import sys
from collections import defaultdict
from appdirs import user_data_dir

menu = {
        'ღორის მწვადი(ერთი შამფური)': 8, 'ხინკალი': 0.5, 'იმერული ხაჭაპური': 5,
        'აჭარული ხაჭაპური': 8, 'ფენოვანი ხაჭაპური': 5, 'ლობიანი': 5, 'ქაბაბი': 3,
        'შემწვარი კარტოფილი': 6, 'ოსტრი': 8, 'შემწვარი ქათამი': 8, 'შემწვარი გოჭი': 30,
        'ლიმონათი': 3, 'წყალი': 1, 'ლუდი': 5
}

keys = list(menu.keys())

print("Menu:")
for i, key in enumerate(keys):
    print(i+1, key, menu[key])

total_price = 0
order_dict = defaultdict(int)


while True:
    try:
        answer = int(input("Enter product number (0 means end order): "))
        if answer == 0:
            print("order ended")
            break
        elif answer in range(1, len(keys)+1):  # აქ +1 სჭირდებოდა რადგან range() ფუნქცია არეინჯებს მითითბულ რიცხვამდე
            product_ordered = keys[answer-1]
            number = int(input("Enter number: "))
            order_dict[product_ordered] += number * menu[product_ordered]
            total_price += number * menu[product_ordered]


    except:
        print("Somthing is wrong! Try again!")

# Determine the user data directory
user_data_directory = user_data_dir("RestourantApp", "Bakar")

# Ensure that the output directory exists
output_dir = os.path.join(user_data_directory, 'output')
os.makedirs(output_dir, exist_ok=True)

# Create the output file path
output_file_path = os.path.join(output_dir, 'order.txt')



print("Order saved in a file:", output_file_path)
with open (output_file_path, 'a') as f:
    for key, value in order_dict.items():
        f.write(f"{key} number: {value/menu[key]} Cost: {value} Gel\n")
    f.write(f"Total: {total_price}\n")

