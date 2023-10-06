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
