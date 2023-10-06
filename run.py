"""
This module defines the SpaceshipGame class
and the main function to run the game.
"""

import os
import random
import time
import sys

def clear_terminal():
    """
    Clear the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.05):
    """
    Display text with a typewriter effect.

    Args:
        text (str): The text to be displayed.
        delay (float, optional): The delay between printing each character.

    Returns:
        None
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

class TitleScreen:
    """
    Represents the title screen of the game.
    """
    def __init__(self):
        self.title = r"""
         _   _      _           _         ____        _   _   _       __                 _   
        | \ | | ___| |__  _   _| | __ _  | __ )  __ _| |_| |_| | ___ / _|_ __ ___  _ __ | |_ 
        |  \| |/ _ \ '_ \| | | | |/ _` | |  _ \ / _` | __| __| |/ _ \ |_| '__/ _ \| '_ \| __|
        | |\  |  __/ |_) | |_| | | (_| | | |_) | (_| | |_| |_| |  __/  _| | | (_) | | | | |_ 
        |_| \_|\___|_.__/ \__,_|_|\__,_| |____/ \__,_|\__|\__|_|\___|_| |_|  \___/|_| |_|\__|
                                                                                                                                            
        """
        self.play_game = None

    def display(self):
        """
        Display the title screen and ask if the user wants to play the game.
        """
        print(self.title)
        while True:
            choice = input("Do you want to play Spaceship Game? (yes/no): ").strip().lower()
            if choice == "yes":
                self.play_game = True
                break
            elif choice == "no":
                self.play_game = False
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

class Board:
    """
    Represents the game board.
    """
    def __init__(self, size):
        """
        Initialize a new game board.

        Args:
            size (int): The size of the square board.
        """
        self.size = size
        self.grid = [['🌫' for _ in range(size)] for _ in range(size)]
        self.guessed_locations = set()
        self.planets = set()

    def display(self, hide_ships=True):
        """
        Display the game board.

        Args:
            hide_ships (bool, optional): Whether to hide the ships on the board. Defaults to True.
        """
        print('  ' + ' '.join(str(i) for i in range(self.size)))
        for i, row in enumerate(self.grid):
            row_display = []
            for j, cell in enumerate(row):
                if (i, j) in self.guessed_locations:
                    row_display.append(cell)
                else:
                    if hide_ships:
                        row_display.append('🌫')
                    else:
                        row_display.append(cell)
            print(f"{i} {' '.join(row_display)}")

    def update(self, x_coordinate, y_coordinate, symbol):
        """
        Update the board with the given symbol at the given coordinates.

        Args:
            x_coordinate (int): The x-coordinate of the cell to be updated.
            y_coordinate (int): The y-coordinate of the cell to be updated.
            symbol (str): The symbol to be placed at the given coordinates.
        """
        self.grid[x_coordinate][y_coordinate] = symbol
        self.guessed_locations.add((x_coordinate, y_coordinate))

    def initialize_planets(self, num_planets):
        """ 
        Initialize the board with the given number of planets.
á
        Args:
            num_planets (int): The number of planets to be placed on the board.
        """
        while len(self.planets) < num_planets:
            x_coordinate = random.randint(0, self.size - 1)
            y_coordinate = random.randint(0, self.size - 1)
            if (x_coordinate, y_coordinate) not in self.planets and \
                self.grid[x_coordinate][y_coordinate] == '🌫':
                self.planets.add((x_coordinate, y_coordinate))
                self.grid[x_coordinate][y_coordinate] = '🪐'

class Ship:
    """
    Represents a spaceship on the board.
    """
    def __init__(self, owner, coordinates):
        """
        Initialize a spaceship.

        Args:
            owner (str): The owner of the spaceship.
            coordinates (list of tuple): The coordinates occupied by the spaceship.
        """
        self.owner = owner
        self.coordinates = coordinates
        self.sunk = False

class User:
    """
    Represents a user in the game.
    """
    def __init__(self, name, board_size, num_ships):
        """
        Initialize a user.

        Args:
            name (str): The name of the user.
            board_size (int): The size of the game board.
            num_ships (int): The number of spaceships the user wants to place.
        """
        self.name = name
        self.board = Board(board_size)
        self.ships = []
        self.num_ships = num_ships
        self.score = 0
        self.ships_sunk = 0
        self.guessed_locations = set()


    def place_ships(self):
        """
        Determine how the user wants to place their spaceships and place them accordingly.
        """
        print(f"{self.name}, how would you like to place your spaceships?")
        print("1. Manually choose ship locations")
        print("2. Have them placed randomly")

        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice == "1":
                self.place_ships_manually()
                break
            elif choice == "2":
                self.place_ships_randomly()
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def place_ships_manually(self):
        """
        Manually place the user's spaceships on the board.
        """
        for ship_number in range(1, self.num_ships + 1):
            message = f"Placing {self.name}'s spaceship {ship_number} out of {self.num_ships}"
            typewriter_effect(message)
            coordinates = []  # List to store ship coordinates
            while True:
                x_coordinate, y_coordinate = self.get_valid_input()
                if (x_coordinate, y_coordinate) not in coordinates and \
                    self.board.grid[x_coordinate][y_coordinate] == '🌫':
                    coordinates.append((x_coordinate, y_coordinate))
                    self.board.grid[x_coordinate][y_coordinate] = '🚀'
                    self.ships.append(Ship(self.name, coordinates))
                    break
                elif (x_coordinate, y_coordinate) in coordinates:
                    print(f"You have already placed spaceship {ship_number} at "
                          f"({x_coordinate}, {y_coordinate}). Try again.")
                else:
                    print("Invalid coordinates or spot already occupied. "
                          "Please choose valid coordinates.")

    def place_ships_randomly(self):
        """
        Place the user's spaceships randomly on the board.
        """
        for _ in range(1, self.num_ships + 1):
            coordinates = []
            while True:
                x_coordinate = random.randint(0, self.board.size - 1)
                y_coordinate = random.randint(0, self.board.size - 1)
                if (x_coordinate, y_coordinate) not in coordinates and \
                    self.board.grid[x_coordinate][y_coordinate] == '🌫':
                    coordinates.append((x_coordinate, y_coordinate))
                    self.board.grid[x_coordinate][y_coordinate] = '🚀'
                    self.ships.append(Ship(self.name, coordinates))
                    print(f"{self.name}'s spaceship placed at ({x_coordinate}, {y_coordinate})")
                    break

    def get_valid_input(self):
        """
        Get valid input for coordinates from the user.

        Returns:
            tuple: A tuple containing the x_coordinate and y_coordinate coordinates.
        """
        while True:
            try:
                input_str = input(f"{self.name}'s Turn: Enter the X and Y coordinates (eg. 2 3): ")
                x_coordinate, y_coordinate = map(int, input_str.split())
                if 0 <= x_coordinate < self.board.size and 0 <= y_coordinate < self.board.size:
                    position = (x_coordinate, y_coordinate)
                    if position not in self.guessed_locations:
                        self.guessed_locations.add(position)
                        return x_coordinate, y_coordinate
                    else:
                        print(f"You have already guessed this spot. Try again, {self.name}.")
                else:
                    print("Invalid coordinates. Please enter coordinates within the board.")
            except ValueError:
                print("Invalid input. Please enter valid numbers for the coordinates.")

class SpaceshipGame:
    """
    Represents a game of Spaceship.
    """
    def __init__(self):
        """
        Initialize the game.
        """
        self.rounds_played = 0

    def play(self):
        """
        Play the game.
        """
        player_name = input("Enter your name: ")
        while True:
            try:
                board_size = int(input("Enter the board size min size = 5 (5x5): "))
                if board_size >= 5:
                    break
                else:
                    print("Board size must be at least 5. Please enter a valid board size.")
            except ValueError:
                print("Invalid input. Please enter a valid integer for the board size.")

        while True:
            try:
                num_ships = int(input("Enter the number of spaceships you want to place: "))
                if num_ships >= 5 and num_ships <= (board_size * board_size) * 0.3:
                    break
                else:
                    print("Number of spaceships must be between 5 and 30% of the board size.")
            except ValueError:
                print("Invalid input. Please enter a valid number of spaceships.")

        player = User(player_name, board_size, num_ships)
        computer = User("Computer", board_size, num_ships)

        typewriter_effect(f"Welcome to Spaceship, {player_name}!")

        player.place_ships()
        self.place_computer_ships(computer, num_ships, board_size)
        player.board.initialize_planets(board_size)  # Initialize planets for the player
        computer.board.initialize_planets(board_size)  # Initialize planets for the computer

        while True:
            time.sleep(1)
            clear_terminal()
            print(f"{player.name}'s Board:")
            player.board.display(False)
            print("\nComputer's Board:")
            computer.board.display(True)

            x_coordinate, y_coordinate = player.get_valid_input()  # Player's Turn
            self.rounds_played += 1

            hit = False
            extra_munitions = False
            for ship in computer.ships:
                for coord in ship.coordinates:
                    if coord == (x_coordinate, y_coordinate):
                        hit = True
                        ship.coordinates.remove(coord)
                        if not ship.coordinates:
                            ship.sunk = True
                            player.score += 1
                            player.ships_sunk += 1
                            message = f"Spaceship at was found ({x_coordinate}, {y_coordinate})."
                            typewriter_effect(message)
                            computer.board.update(x_coordinate, y_coordinate, '💥')
                            break

            if not hit:
                for planet in computer.board.planets:
                    if planet == (x_coordinate, y_coordinate):
                        extra_munitions = True
                        message = "Extra munitions found, take another guess!"
                        typewriter_effect(message)
                        computer.board.update(x_coordinate, y_coordinate, '🪐')
                        break

            if not hit and not extra_munitions:
                message = f"You shot and found nothing at ({x_coordinate}, {y_coordinate})."
                typewriter_effect(message)
                computer.board.update(x_coordinate, y_coordinate, 'M')

            if extra_munitions:
                continue

            if all(ship.sunk for ship in computer.ships):
                typewriter_effect(f"{player.name} has sunk {player.score}/{num_ships}")
                typewriter_effect(f"In {self.rounds_played} rounds. Congratulations!")
                display_win_art()  # Display win text art
                break

            x_coordinate, y_coordinate = self.computer_make_guess(player.board.size, player.board)
            self.rounds_played += 1

            message = f"Computer's Turn: Attempted shot at ({x_coordinate}, {y_coordinate})."
            typewriter_effect(message)

            hit = False
            for ship in player.ships:
                for coord in ship.coordinates:
                    if coord == (x_coordinate, y_coordinate):
                        hit = True
                        ship.coordinates.remove(coord)
                        if not ship.coordinates:
                            ship.sunk = True
                            computer.score += 1
                            message = f"Spaceship at was found ({x_coordinate}, {y_coordinate})."
                            typewriter_effect(message)
                            player.board.update(x_coordinate, y_coordinate, '💥')
                            break

            if not hit:
                for planet in player.board.planets:
                    if planet == (x_coordinate, y_coordinate):
                        message = "Extra munitions found, take another guess!"
                        typewriter_effect(message)
                        player.board.update(x_coordinate, y_coordinate, '🪐')
                        break

            if not hit and not extra_munitions:
                message = f"Computer shot and found nothing at ({x_coordinate}, {y_coordinate})."
                typewriter_effect(message)
                player.board.update(x_coordinate, y_coordinate, 'M')

            if extra_munitions:
                continue

            if all(ship.sunk for ship in player.ships):
                typewriter_effect(f"Computer has sunk {computer.score}/{num_ships}")
                typewriter_effect(f"In {self.rounds_played} rounds. Better luck next time!")
                display_loss_art()  # Display loss text art
                break

    def computer_make_guess(self, board_size, player_board):
        """
        Generate a random guess for the computer.

        Args:
            board_size (int): The size of the game board.
            player_board (Board): The player's game board.

        Returns:
            tuple: A tuple containing the x_coordinate and y_coordinate of the guess.
        """
        pass

    def place_computer_ships(self, computer, num_ships, board_size):
        """
        Place the computer's spaceships on the board.

        Args:
            computer (User): The computer player.
            num_ships (int): The number of spaceships to place.
            board_size (int): The size of the game board.
        """
        pass
def display_win_art():
    """
    Display a winning message in ASCII art.
    """
    pass

def display_loss_art():
    """
    Display a losing message in ASCII art.
    """
    pass

def main():
    """
    Define the main function to run the game.
    """
    pass

if __name__ == "__main__":
    main()
