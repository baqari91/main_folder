from random import randint, choice


class Ship:
    def __init__(self, name, positions):
        self.name = name
        self.positions = positions
        self.destroyed = [False] * len(positions)


class Game:
    probable_computer_positions = [
        [Ship("Maverick", [3]), Ship("Gunner", [8, 9]), Ship("Matilda", [13, 14, 15])],
        [Ship("Maverick", [4]), Ship("Gunner", [10, 11]), Ship("Matilda", [16, 17, 18])],
        [Ship("Maverick", [5]), Ship("Gunner", [12, 13]), Ship("Matilda", [18, 19, 20])]
    ]

    def __init__(self):
        self.computer_positions = []
        self.player_positions = []
        self.setup_player_ships()
        self.game_playing = True
        self.player_destroyed_ship = 0
        self.computer_destroyed_ship = 0
        self.generate_random_ships()

    def generate_random_ships(self):
        random_computer_positions = choice(Game.probable_computer_positions)
        self.computer_positions.extend(random_computer_positions)

    def setup_player_ships(self):
        ship_positions = [
            (input("Ship Name: "), [int(input("Position: "))]),
            (input("Medium Ship Name: "), list(map(int, input("Enter positions as a range (e.g., 4-5): ").split("-")))),
            (input("Big Ship Name: "), list(map(int, input("Enter positions as a range (e.g., 7-9): ").split("-")))),
        ]
        for name, positions in ship_positions:
            self.player_positions.append(positions)

    @staticmethod
    def check_ship_hit(ship_positions, target):
        for idx, positions in enumerate(ship_positions):
            if target in positions:
                ship_positions[idx][positions.index(target)] = "x"

                return True
        return False

    def play_game(self):
        while self.game_playing:
            computer_shoot = randint(1, 20)
            if self.check_ship_hit(self.player_positions, computer_shoot):
                print(f"Computer hit at position: {computer_shoot}")
                self.player_destroyed_ship += 1

            player_shoot = int(input("Enter position to fire (1-20): "))
            if self.check_ship_hit([ship.positions for ship in self.computer_positions], player_shoot):
                print(f"You hit the computer at position: {player_shoot}")
                self.computer_destroyed_ship += 1

            if self.player_destroyed_ship == 6:
                self.game_playing = False
                print("Computer wins!")
            if self.computer_destroyed_ship == 6:
                self.game_playing = False
                print("Congratulations! You won!")


if __name__ == "__main__":
    game = Game()
    game.play_game()
