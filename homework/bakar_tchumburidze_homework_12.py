"1. დაწერე ფუნქცია რომელიც მიიღებს ლექსიკონს და ამოშლის მასში ყველა დუბლირებულ ინფორმაციას."

my_dict1 = {'a': 1, 'b': 2, 'c': 2}
def unique_dict(dict1):
    unique_dict = {}
    for key,value in dict1.items():
        if value not in unique_dict.values():
            unique_dict[key] = value
    return unique_dict
result_dict = unique_dict(my_dict1)
print(result_dict)

"2. დაწერე ფუნქცია რომელიც მიიღებს ლექსიკონს და შეამოწმებს ცარიელია თუ არა ის (დააბრუნებს True თუ ცარიელია ან False_ს თუ არაა ცარიელი."

my_dict2 = {}
def check_dict(dict2):
    return len(dict2) == 0
print(check_dict(my_dict2))

"""3. დაწერე ფუნქცია რომელიც მიიღებს სტრიქონის ტიპის მონაცემს, შექმნის მისგან ლექსიკონს და დააბრუნებს. (ლექსიკონის გასაღები სტრიქონში არსებული სიმბოლოებია, მნიშვნელობები კი განმეორების რაოდენობა. 
მაგ: 'w3schools'
Expected output: {'w': 1, '3': 1, ‘s': 2, ‘c': 1, ‘h': 1, 'o': 2, ‘l': 1}"""

from collections import defaultdict

a = 'striqoni'
def create_dict(dict3):
    my_dict3 = defaultdict(str)
    for i in dict3:
        my_dict3[i] = dict3.count(i)
    return my_dict3
print(create_dict(a))


"4. დაწერე ფუნქცია რომელიც მიიღებს ლექსიკონს და დააბრუნებს  ერთ სიაში გაერთიანებულ key, value წყვილებს."

my_dict4 = {'a':1,'b':2,'c':3}
def dict_to_list(dict4):
    created_list = []
    for k,v in dict4.items():
        created_list.append(k)
        created_list.append(v)
    return created_list
print(dict_to_list(my_dict4))
        






