from abc import abstractmethod, ABCMeta
from typing import ClassVar 
from dataclasses import dataclass , field
from random import randint , choice  
from entity import Character
from inventory import Inventory
from colors import bcolors

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
