#დავალება
#ლექსიკონების დახმარებით შექმენი პითონში პროგრამა, რომელიც წარგიდგენს რესტორნის მენიუს. მიიღებს შეკვეთას.
# შექმნის ფაილს და ჩაწერს შეკვეთასა და მის ღირებულებას. პროგრამა გადააქციე exe ფაილად და დაუყენე რესტორნის სურათი.

from collections import defaultdict

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
        elif answer in range(1, len(keys)):
            product_ordered = keys[answer-1]
            number = int(input("Enter number: "))
            order_dict[product_ordered] += number * menu[product_ordered]
            total_price += number * menu[product_ordered]


    except:
        print("Somthing is wrong! Try again!")

print("Order:")
for key, value in order_dict.items():
    print(f"{key} number: {value/menu[key]} Cost: {value} Gel")
print("Total:", total_price)