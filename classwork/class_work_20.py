import json
with open('states.json') as file_state:
    data = json.load(file_state)
print(data)