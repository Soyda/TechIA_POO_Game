from dataclasses import dataclass, field
from typing import ClassVar
from abc import ABCMeta, abstractmethod
import os
from class_inventory import Inventory
from class_entity import Player
from class_score import Score 

@dataclass
class Game:
    player_name : str = field(init=False)
    score : object = field(init=False)
    main_choice : str = field(init=False)
    exit : bool = True

    def get_player_name(self):
        self.player_name = input("What's name your name friend ?\n")
        return self.player_name

    def main_menu(self):
        while(self.exit):
         
            self.main_choice = input(f"\nMain menu : \n Make your choice {self.player_name} (Use number 1 - 2 - 3) \n 1 - Start  \n 2 - Score \n 3 - Exit \n ")

            if self.main_choice == '1':

                player = Player(self.player_name, 50, 1)
                inventory = Inventory(3, 1, 3, 20)

                print("-----------------------------------------------------------------------------------------")
                print(f"Hi {player.name} !! We need your help!")
                print(f"The kingdom is under attack! Defend the kingdom of VS Code, all depends on your abilities.")
                print("-----------------------------------------------------------------------------------------")

                print(f'Your starting stats are:\n Name: {player.name}\n HP: {player.HP}\n Level: {player.lvl}\n')
                inventory.check_inventory()

                # combat = Combat()
                # shop

            elif self.main_choice == '2':
                self.score = Score(self.player_name, 0)
                self.score.display_score()

            elif self.main_choice == '3':
                print("See you later !")
                self.exit = False
            
            else :
                print("Please use number 1, 2, or 3")

game = Game
game.get_player_name(game)
game.main_menu(game)
