from random import choice


class Ship:
    def __init__(self, name, positions):
        self.name = name
        self.positions = positions
    def __repr__(self):
        return f'{self.name}, {self.positions}'


probable_computer_positions = [
        [Ship("Maverick", [3]), Ship("Gunner", [8, 9]), Ship("Matilda", [13, 14, 15])],
        [Ship("Maverick", [4]), Ship("Gunner", [10, 11]), Ship("Matilda", [16, 17, 18])],
        [Ship("Maverick", [5]), Ship("Gunner", [12, 13]), Ship("Matilda", [18, 19, 20])]
    ]
computer = choice(probable_computer_positions)
print(computer)

help(computer.extend)