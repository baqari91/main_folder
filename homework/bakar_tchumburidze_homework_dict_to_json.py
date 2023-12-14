import json

def create():
    di = {}

    user_name = input("enter username: ")
    di[user_name] = None

    name = input("enter your name: ")
    di[user_name] = [name]

    age = input("ebter your age: ")
    di[user_name].append(age)

    with open('data_json.json', 'w') as file:
        json.dump(di, file)
        print("new data is saved in a file 'data_json.json")
    return di




def edit_json_file():
    with open('data_json.json', 'r') as file:
        data = json.load(file)
    found = False
    while not found:
        try:
            key_to_update = input("enter your username: ")
            print(f'your name is: {data[key_to_update][0]} \n your age: {data[key_to_update][1]}')

            if key_to_update in data:
                new_name = input('enter new name: ')
                data[key_to_update] = [new_name]

                new_age = input('enter new age: ')
                data[key_to_update].append(new_age)
                found = True
        except:
            print("მითითებული username არ არსებობს")


    with open('data_json.json', 'w') as file:
        json.dump(data, file)
        print("new data is saved in a file 'data_json.json")

    return data








