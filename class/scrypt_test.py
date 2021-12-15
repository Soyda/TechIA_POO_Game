from abc import abstractmethod, ABCMeta
import os 
import pickle
from typing import ClassVar 
from dataclasses import dataclass , field
from random import randint , choice  
import csv 
import colorama
from pickle import * 
import os.path 

@dataclass 
class Character(metaclass=ABCMeta):
    name : str 
    HP : int 
    lvl : int 
    is_dead : bool = False 
    list_enemies : list = field(default_factory=list)
    
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value):
        self._name = value 

    @property
    def HP(self) -> int:
        return self._HP
    @HP.setter
    def HP(self,value):
        if not isinstance(value,int):
            raise ValueError('HP should be an int')
        else:
            self._HP = value

    @property
    def lvl(self) -> int:
        return self._lvl
    @lvl.setter
    def lvl(self,value):
        if not isinstance(value,int):
            raise ValueError('lvl should be an int')
        else:
            self._lvl = value 
        
    def check_hp(self) :
        ''' Function to chek enemies life
        if enemy is dead set HP to 0 and switch bool True    
        ---------------  
        '''
        
        count = 0  
        if len(self.list_enemies)>0 :
            for i in self.list_enemies :
                if i['HP'] <= 0 :
                    i['HP'] = 0 
                    i['is_dead'] = True 
                    count += 1 
        if self.HP <= 0 :
            self.is_dead = True 
        
            


@dataclass
class Enemies(Character):

    @staticmethod
    def enemy_attack(player):
        ''' Function for enemy attack   
        ---------------  
        player should be instance of Player Class'''
        player.HP -= randint(4,9)
        return player.HP
    def gen(self):
        ''' Function to create and add random enemies
         and add them into a list
        ---------------  
        '''
        c=0 
        name_list= ["Pythosore","Devosore","Simplosore","Tiranosor","Bigbob","Jevaismourir"]
        self.list_enemies.append({"Name" : self.name , "HP" : self.HP, 'Level' : self.lvl , 'is_dead' : self.is_dead})
        while c < randint(2,3):
            self.list_enemies.append({ "Name" : choice(name_list) , "HP" : randint(25,40), 'Level' : self.lvl , 'is_dead' : self.is_dead})
            c += 1 
        return self
    def unique(self):
        ''' Function to add this instance into the list_enemies
        ---------------  
        '''
        self.list_enemies.append({"Name" : self.name , "HP" : self.HP, 'Level' : self.lvl , 'is_dead' : self.is_dead})
        return self

@dataclass
class Inventory(metaclass=ABCMeta):
    potion : int
    max_potion : int
    mana_potion : int
    gold : int 

    def add_potion(self):
        '''This function increase the number of potion by one'''
        self.potion += 1

    def remove_potion(self):
        '''This function decrease the number of potion by one'''
        self.potion -= 1

    def add_max_potion(self):
        '''This function increase the number of max potion by one'''
        self.max_potion += 1

    def remove_max_potion(self):
        '''This function decrease the number of max potion by one'''
        self.max_potion -= 1
    
    def add_mana_potion(self):
        '''This function increase the number of mana potion by one'''
        self.mana_potion += 1

    def remove_mana_potion(self):
        '''This function decrease the number of mana potion by one'''
        self.mana_potion -= 1

    def add_gold(self, value):
        '''This function increase the number of potion by one'''
        self.gold += value

    def remove_gold(self, value):
        '''This function decrease the number of potion by one'''
        self.gold -= value

    def check_inventory(self,player):
        '''This function prints the number of potions available in inventory'''
        return print(f"\n-----------------------\n Inventory:\n Gold: {player.gold}\n Health potion(s): {player.potion}\n Max health potion(s): {player.max_potion}\n Mana potion(s): {player.mana_potion}\n Gold : {player.gold}\n-----------------------\n")

# inventory = Inventory(10, 2, 3, 100)
# print(inventory.potion)
# print(inventory.max_potion)
# print(inventory.mana_potion)
# print(inventory.gold)
# inventory.check_inventory()
# inventory.add_max_potion()
# inventory.add_potion()
# inventory.add_mana_potion()
# inventory.add_gold(150)
# inventory.check_inventory()
# inventory.remove_max_potion()
# inventory.remove_potion()
# inventory.remove_mana_potion()
# inventory.remove_gold(75)
# inventory.check_inventory()

@dataclass
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    BLUE = '\033[34m' #BLUE
    RESET = '\033[0m' #RESET COLOR



@dataclass
class Player(Character,Inventory):
    mana : int = 250


    def attack_big_punch(self,enemy, target, combat) : 
        ''' Function to attack enemy by random between 5 and 10   
        ---------------  
        x should be an int  (Like x = enemy[HP]) '''
        if self.mana >= 10 :
            self.mana -= 10 
            diff_enemy = enemy.list_enemies[target - 1]["HP"] 
            enemy.list_enemies[target - 1]['HP'] -= randint(9,14)
            print(bcolors.FAIL + "\n Good shot! Enemy loose : -", diff_enemy - enemy.list_enemies[target - 1]["HP"], " HP" + bcolors.RESET)
            diff = self.HP
            self.HP = enemy.enemy_attack(self)
            print(bcolors.FAIL + f"\n Oh, now you are under attack!! \n{self.name} : -", diff - self.HP, "HP lost!" ,"\n" + bcolors.RESET) 
            combat.round += 1 
            print(f'=================================  ROUND {combat.round}   ================================\n')
            
            return enemy.list_enemies[target - 1]['HP']
        else:
            print('You didnt have enough mana')
            return enemy.list_enemies[target - 1]['HP']

    def attack_lightning(self,enemy, target, combat):
        ''' Function to attack one enemy by random damages between 9 and 12
        Mana player is decreased by 50  
        ---------------  
        x should be an int  (Like x = enemy[HP])   '''
        if self.lvl >= 3 :
            if self.mana >= 50 :
                self.mana -= 50 
                diff_enemy = enemy.list_enemies[target - 1]["HP"] 
                enemy.list_enemies[target - 1]['HP']-= randint(14,18)
                
                print(bcolors.FAIL + "\n Good shot! Enemy loose : -", diff_enemy - enemy.list_enemies[target - 1]["HP"], " HP" + bcolors.RESET)
                diff = self.HP
                self.HP = enemy.enemy_attack(self)
                print(bcolors.FAIL + f"\n Oh, now you are under attack!! \n{self.name} : -", diff - self.HP, "HP lost!" ,"\n" + bcolors.RESET) 
                combat.round += 1 
                print(f'=================================  ROUND {combat.round}   ================================\n')
            
                return enemy.list_enemies[target - 1]['HP']
            else:
                print('You don\'t have enough mana')
                return enemy.list_enemies[target - 1]['HP']
        else:
            print('You need to reach the level 3 for attack lightning')
            return enemy.list_enemies[target - 1]['HP']
   
    def fire_ball(self,enemy, combat):
        ''' Function to attack a group of enemies by random damages between 8 and 16
        Mana player is decreased by 75  
        ---------------  
        x should be an int  (Like x = enemy[HP])   '''
        if self.lvl >= 3 :
            if self.mana >= 75 :
                self.mana -= 75 
                for i,j in enumerate(enemy.list_enemies):
                    diff_enemy = enemy.list_enemies[i]["HP"] 
                    enemy.list_enemies[i]['HP']-= randint(10,15)
                    
                    print(bcolors.FAIL + "\n Good shot! Enemy loose : -", diff_enemy - enemy.list_enemies[i]["HP"], " HP" + bcolors.RESET)
                diff = self.HP
                self.HP = enemy.enemy_attack(self)
                print(bcolors.FAIL + f"\n Oh, now you are under attack!! \n{self.name} : -", diff - self.HP, "HP lost!" ,"\n" + bcolors.RESET) 
                combat.round += 1 
                print(f'=================================  ROUND {combat.round}   ================================\n')
                for i,j in enumerate(enemy.list_enemies):
                    return enemy.list_enemies[i]['HP']
            else:
                print('You don\'t have enough mana')
                for i,j in enumerate(enemy.list_enemies):
                    return enemy.list_enemies[i]['HP']
        else:
            print('You need to reach the level 5 for fire ball')
            for i,j in enumerate(enemy.list_enemies):
                return enemy.list_enemies[i]['HP']
        
        

    def use_potion(self):
        '''  This function add 15HP to Player.HP '''
        if self.potion >= 1 :
            self.potion -=1 
            self.HP += 15 
            print(bcolors.WARNING + f'\n1 potion used\nNow you have {self.HP} HP' + bcolors.RESET)
        else:
            print("You didn't have enough potion")
        return self.HP 
        

    def use_maxi_potion(self):
        '''  This function add 50HP to Player.HP  '''
        if self.max_potion >= 1 :
            self.max_potion -= 1 
            self.HP += 50 
            print(bcolors.WARNING + f'\n1 max potion used\nNow you have {self.HP} HP' + bcolors.RESET)
        else:
            print("You didn't have enough max potion")
        return self.HP

    def use_mana_potion(self):
        '''  This function add 200mana to Player.mana  '''
        if self.mana_potion >= 1 :
            self.mana_potion -= 1
            self.mana += 200 
            print(bcolors.WARNING + f'\n1 mana potion used\nNow you have {self.mana} Mana' + bcolors.RESET)
        else:
            print("You didn't have enough potion")
        return self.mana



@dataclass
class Shop(Inventory):
    inventory : Inventory = field(init=False)
    Inventory.potion = 5
    Inventory.max_potion = 6
    Inventory.mana_potion = 9
    gold_stock : int = 200
    shop_choice : str = field(init=False)
    sell_choice : str = field(init=False)
    leave : bool = True
    leave_sell : bool = True

    def black_market(self,player):
        while(self.leave):
            self.check_inventory(player)
            print('Welcome my friend, I have some stuff there for you!\n')
            print(f"1. Buy health potion for 20 gold.     ==> {Inventory.potion} item in stock" )
            print(f"2. Buy max health potion for 50 gold. ==> {Inventory.max_potion} item in stock")
            print(f"3. Buy Mana potion for 30 gold.       ==> {Inventory.mana_potion} item in stock")
            print(f"4. Sell an item.")
            print("5. Leave shop.\n")
            self.shop_choice = input("What is your choice ?\n")

            if self.shop_choice == '1':
                if  Inventory.potion > 0 and player.gold >= 20:
                    Inventory.potion -=1 
                    player.potion += 1
                    player.gold -= 20
                    self.gold_stock += 20
                    print("\nA health potion has been added to your inventory.")
                else :
                    print("\nSorry, you can't buy this item for the moment.")
            elif self.shop_choice == '2':
                if Inventory.max_potion > 0 and player.gold >= 50:
                    Inventory.max_potion -= 1
                    player.max_potion += 1
                    player.gold -= 50
                    self.gold_stock += 50
                    print("\nA max health potion has been added to your inventory.")
                else :
                    print("\nSorry, you can't buy this item for the moment.")
            elif self.shop_choice == '3':
                if Inventory.mana_potion >0 and player.gold >= 30:
                    Inventory.mana_potion -= 1
                    player.mana_potion += 1
                    player.gold -= 30
                    self.gold_stock += 30
                    print("\nA mana health potion has been added to your inventory.")
                else :
                    print("\nSorry, you can't buy this item for the moment.")
            elif self.shop_choice == '4':
                while(self.leave_sell):
                    player.check_inventory(player)
                    print(f"\nShop has {self.gold_stock} gold.\n")
                    print(f"1. Sell a health potion for 10 gold.")
                    print(f"2. Sell a max health potion 25 gold.")
                    print(f"3. Sell a mana potion 15 gold.")
                    print(f"4. Back to shop.\n")
                    self.sell_choice = input("What is your choice ?\n")

                    if self.sell_choice == '1':
                        if player.potion > 0 and self.gold_stock >= 10:
                            Inventory.potion += 1
                            player.potion -= 1
                            player.gold += 10
                            self.gold_stock -= 10
                            print(f"\nYou got 10 gold.\nNow you have {player.gold} gold.")
                        else :
                            print("\nSorry, we can't buy this item for the moment.")
                    elif self.sell_choice == '2':
                        if player.max_potion > 0 and self.gold_stock >= 25:
                            Inventory.max_potion += 1 
                            player.max_potion -= 1
                            player.gold += 25
                            self.gold_stock -= 25
                            print(f"\nYou got 25 gold.\nNow you have {player.gold} gold.")
                        else :
                            print("Sorry, we can't buy this item for the moment.")
                    elif self.sell_choice == '3':
                        if player.mana_potion > 0 and self.gold_stock >= 15:
                            Inventory.mana_potion += 1 
                            player.mana_potion -= 1
                            player.gold += 15
                            self.gold_stock -= 15
                            print(f"You got 15 gold.\nNow you have {player.gold} gold.")
                        else :
                            print("Sorry, we can't buy this item for the moment.")
                    elif self.sell_choice == '4':
                        # self.leave_sell = False
                        break
                    else :
                        print("Please use number 1, 2, 3, or 4.")

            elif self.shop_choice == '5':
                # self.leave = False
                break
            else : 
                print("Please use number 1, 2, 3, 4 or 5.")

# inventory = Inventory(5, 2, 3, 200)
# shop = Shop(inventory)
# shop.black_market(shop)
@dataclass
class Score():
    name: str # = field(init=False)
    score: int # = field(init=False)

    # def __post_init__(self):
    #     self.name = player_name 
    #     self.score = round

    def save_score(self, path='./data/scores.csv' ):
        if os.path.exists(path) == False : # check whether scores.csv exists, if not create it 
            header = ["Name", "Score"]
            with open(path, 'w') as score_csv: # create scores.csv
                writer = csv.writer(score_csv, delimiter=',')
                writer.writerow(header) # write the header


        # Update scores.csv
        with open(path, 'a', newline='') as score_csv: # add a new line in csv file
            writer = csv.writer(score_csv, delimiter=',')
            score_line = [self.name, self.score]
            writer.writerow(score_line) # add a line with current name and score
    
    def display_score(self, path='./data/scores.csv'):
        if os.path.exists(path) == False :
            print("==================================")
            print('Sorry no scores available for now.')
            print("==================================")

        else :
            print("==================================")
            # Display scores
            with open(path) as score_csv:
                reader = csv.reader(score_csv, delimiter=',') #reader mode
                for ligne in reader: # read each line
                    if len(ligne) != 0 :
                        print(ligne[0], ' ', ligne[1])
            print("==================================")


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



@dataclass
class Combat(Enemies):
    combat_status : bool = True
    leave : bool = True 
    round : int = 0
    
    def battle_choice(self):
        choice = input ("Make your choice : \n  1 : Attack \n  2 : Inventaire \n  3 : Black market \n  4 : Leave the game  \n")
        return choice
    
    def enemy_choice(self,player,enemy):
        cnt = 1
        for monster in enemy.list_enemies: # we show how to target the ennemy
            print("Please use key " + str(cnt) + " for => " + monster["Name"] + " " + str(monster["HP"]))
            cnt+=1
            
        index = int(input(f"{player.name} : Who do you want to shoot ?")) # we ask the player to target the enemy he wants to attack 
        return index
    
    
    def target_choice(self, player,enemy):
        if player.lvl < 3 :
            attack_choice = input (f"Choose your attack {player.name} ? \n 1 : Big punch \n 2 : Attack lightning"+ bcolors.WARNING + "  (Unlock level 3)" +bcolors.RESET + " \n 3 : Fire ball        " + bcolors.WARNING + " (Unlock level 5) " + bcolors.RESET)
        elif 3 <= player.lvl < 5 :
            attack_choice = input (f"Choose your attack {player.name} ? \n 1 : Big punch \n 2 : Attack lightning \n 3 : Fire ball" + bcolors.WARNING + "    (Unlock level 5) " + bcolors.RESET)
        else:
            attack_choice = input (f"Choose your attack {player.name} ? \n 1 : Big punch \n 2 : Attack lightning \n 3 : Fire ball \n ")
        
        if attack_choice == "1":
            target = int(self.enemy_choice(player,enemy))
            player.attack_big_punch(enemy, target, self)

        elif attack_choice == "2":
            target = int(self.enemy_choice(player,enemy))
            player.attack_lightning(enemy,target, self)

        elif attack_choice == "3":
            player.fire_ball(enemy,self)
            
        else:          
            print("Use correct number")
            self.target_choice(player,enemy)
    
    def battle(self,player,enemy,game):
        while self.leave :
            game.combat_leave_option = '0' # reset this value so that loop doesn't break

            print(bcolors.BLUE + f" Enemies in game : \n------------------" + bcolors.RESET)

            for i in enemy.list_enemies:
                print(bcolors.BLUE + f" Monster : {i['Name']}   //   Lvl : {i['Level']}   //  HP : {i['HP']}" + bcolors.RESET)
            print(bcolors.WARNING + f'\n        Player stats :\n===============================\n         Name: {player.name}\n         HP: {player.HP}\n         Level: {player.lvl}\n         Mana: {player.mana} ' + bcolors.RESET)
            question = self.battle_choice()
            if question == "1" : # we start the attack against enemies
                self.target_choice(player,enemy)
                player.check_hp()
                enemy.check_hp()
                count = 0 
                for i in enemy.list_enemies:
                    if i['is_dead'] == True :
                        count += 1 
                if len(enemy.list_enemies) == count :
                    print('You beat this wave!')
                    player.lvl += 1 
                    player.HP += 1
                    player.mana += 165
                    break
                if player.is_dead == True :
                    print(f'You are dead {player.name}.. Try again')
                    break
                        
            elif question == "2" : # we start the inventory menu
                while True :
                    player.check_inventory(player)
                    menu = input(f' Inventory menu: \n 1. Use potion : {player.potion} \n 2. Use max potion : {player.max_potion} \n 3. Use mana potion : {player.mana_potion} \n 4. Exit \n')
                    if menu == "1":
                        player.use_potion()
                    if menu == "2" :
                        player.use_maxi_potion()
                    if menu == "3":
                        player.use_mana_potion()
                    if menu == "4":
                        break
            elif question == "3" : # we create the Shop instance
                Shop(10,10,10,10).black_market(player)
            elif question == "4":
                game.combat_leave_option = input('1. Leave and save\n2. Leave\n')
                break
            else:
                print(bcolors.FAIL + "Please use correct number \n" + bcolors.RESET)

# enemies = Enemies('mini_boss', 75,5).gen()
# Fight = Combat(0,enemies)
# Fight.battle()



def main (game):
    game.main_menu(game)
    main(Game)

main(Game)