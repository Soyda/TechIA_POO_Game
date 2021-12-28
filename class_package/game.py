from dataclasses import dataclass, field
import os
from class_package.inventory import Inventory
from class_package.character import Player
from class_package.score import Score 
from class_package.entity import Enemies
from class_package.combat import Combat
import pickle 
from class_package.colors import bcolors


@dataclass
class Game:
    player_name : str = field(init=False)
    score : object = field(init=False)
    wave : int = field(init=False)
    combat_leave_option: str = '0'
    exit : bool = True
    save : bool = False 
    

    def get_player_name(self):
        self.player_name = input("What's your name friend ?\n")
        return self.player_name

    def get_enemies(self,enemies):
        if self.wave == 1:
            enemies = Enemies('First Captain', 55, 1).gen()
        elif self.wave == 2:
            enemies = Enemies('First boss', 125, 1).unique()
        elif self.wave == 3:
            enemies = Enemies('Second Captain', 75,2).gen()
        elif self.wave == 4:
            enemies = Enemies('Second boss', 225, 2).unique()
        elif self.wave > 4 :
            enemies = Enemies('Infiny Captain', 30 * self.wave,3).gen()
        return enemies

    

    def main_menu(self):
        while(self.exit):
            
            main_choice = input(f"\nMain menu \nMake your choice: (Use number 1 - 2 - 3) \n 1 - {'New game' if self.save == False else 'Continue game'}  \n 2 - Load game \n 3 - Score \n 4 - Exit \n ")

            if main_choice == '1':
                self.get_player_name(Game) if self.save == False else self.player_name 
                player = Player(3,1,3,250,self.player_name,155,8, mana=5550) if self.save == False else player
                print("===================================================================================================")
                print(f"The kingdom is under attack! Defend the kingdom of VS Code, all depends on your abilities {self.player_name}.")
                print("===================================================================================================")
                

                wave_continue = True
                self.wave = 1 if self.save == False else self.wave
                while wave_continue :
                    print("\n===========================================================================")
                    print(f'=================================  WAVE {self.wave}  ================================')
                    print("===========================================================================")

                    enemies = object
                    enemies = self.get_enemies(self,enemies)

                    Combat(enemies.name, enemies.HP , enemies.lvl + self.wave ).battle(player,enemies, self)

                    if self.combat_leave_option == '1':
                        f = open('./data/save.csv', 'wb')
                        pickle.dump([player,enemies,self.wave,self.player_name],f)
                        f.close()
                        print("Your game has been saved.")
                        break
                    elif self.combat_leave_option == '2':
                        break

                    self.wave += 1

                self.score = Score(player.name, self.wave)
                self.score.save_score()

            elif main_choice == '2':
                file = './data/save.csv'
                save = open(file,"rb")
                variable = pickle.load(save)
                print(variable)
                player = variable[0]
                enemies = variable[1]
                self.wave = variable[2]
                self.player_name = variable[3]
                save.close()
                choice = input(f'Saved game : \n1 - Name : {player.name}\nPress the number of your save here : ')
                if choice == "1":
                    if os.path.isfile(file):
                        self.save = True 

            elif main_choice == '3':
                self.score = Score(self.player_name, 0)
                self.score.display_score()

            elif main_choice == '4':
                print("See you later !")
                self.exit = False
            else :
                print(bcolors.FAIL + "\n Please use number 1, 2, 3 or 4" + bcolors.RESET)
