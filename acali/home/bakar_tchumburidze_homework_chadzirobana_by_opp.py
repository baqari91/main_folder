from random import randint, choice

class Ship:
    def __init__(self, name, positions):
        self.name = name
        self.positions = positions
        self.destroyed = [False] * len(positions)

class Game:
    computer_positions1 = [
        ["Maverick", [3]], ["Gunner", [8, 9]], ["Matilda", [13, 14, 15]],
        ["Maverick", [4]], ["Gunner", [10, 11]], ["Matilda", [16, 17, 18]],
        ["Maverick", [5]], ["Gunner", [12, 13]], ["Matilda", [18, 19, 20]]
    ]
    computer = choice(computer_positions1)
    def __init__(self):
        self.computer_positions = [
            self.computer
        ]
        self.player_positions = []
        self.setup_player_ships()
        self.game_playing = True
        self.player_destroyed_ship = 0
        self.computer_destroyed_ship = 0

        print(self.computer_positions)

    def setup_player_ships(self):
        ship_positions = [
            (input("Ship Name: "), int(input("Position: "))),
            (input("Medium Ship Name: "), int(input("Start position, add next number: "))),
            (input("Big Ship Name: "), int(input("Start position, add next 2 numbers: ")))
        ]
        for _, positions in ship_positions:
            self.player_positions.append(positions if isinstance(positions, list) else [positions])
        print(ship_positions)
    def check_ship_hit(self, ship_positions, target):
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


            if self.player_destroyed_ship == 3:
                self.game_playing = False
                print("Congratulations! You won!")
            if self.computer_destroyed_ship == 3:
                self.game_playing = False
                print("Computer wins!")

if __name__ == "__main__":
    game = Game()
    game.play_game()
