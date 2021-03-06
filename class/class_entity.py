from abc import abstractmethod, ABCMeta
from typing import ClassVar 
from dataclasses import dataclass , field
from random import randint , choice  

 
@dataclass 
class Character(metaclass=ABCMeta):
    name : str
    HP : int 
    lvl : int 
    is_dead : bool = False 
    list_enemies : list = field(default_factory=list)
    status = True 
    
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value,str):
            raise ValueError('name should be a string')
        else:
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
            return f"{str(count) + ' player is dead' if count == 1 else str(count) + ' players are dead' }" 
        if len(self.list_enemies) == count:
            self.status = False 
        if self.HP <= 0 :
            self.status = False 
            self.is_dead = True 
            return f'You are dead.. Try again {self.name}'
        
            


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
            self.list_enemies.append({ "Name" : choice(name_list) , "HP" : randint(35,50), 'Level' : self.lvl , 'is_dead' : self.is_dead})
            c += 1 
        return self
    def unique(self):
        ''' Function to add this instance into the list_enemies
        ---------------  
        '''
        self.list_enemies.append({"Name" : self.name , "HP" : self.HP, 'Level' : self.lvl , 'is_dead' : self.is_dead})
        return self




@dataclass
class Player(Character):
    mana : int = 250


    def attack_big_punch(self,x) : 
        ''' Function to attack enemy by random between 5 and 10   
        ---------------  
        x should be an int  (Like x = enemy[HP]) '''
        if self.mana >= 10 :
            self.mana -= 10 
            x-= randint(5,10)
            return x
        else:
            print('You didnt have enough mana')

    def attack_lightning(self,x):
        ''' Function to attack one enemy by random damages between 9 and 12
        Mana player is decreased by 50  
        ---------------  
        x should be an int  (Like x = enemy[HP])   '''
        if self.lvl >= 3 :
            if self.mana >= 50 :
                self.mana -= 50 
                x-= randint(9,12)
                return x
            else:
                print('You didnt have enough mana')
        else:
            print('You need reach the level 3 for attack lightning')

   
    def fire_ball(self,x):
        ''' Function to attack a group of enemies by random damages between 8 and 16
        Mana player is decreased by 75  
        ---------------  
        x should be an int  (Like x = enemy[HP])   '''
        if self.lvl >= 3 :
            if self.mana >= 75 :
                self.mana -= 75 
                x-= randint(8,16)
                return x 
            else:
                print('You didnt have enough mana')
        else:
            print('You need reach the level 5 for fire ball')
        

    def use_potion(self):
        '''  This function add 15HP to Player.HP '''
        self.HP += 15 
        return self.HP 

    def use_maxi_potion(self):
        '''  This function add 50HP to Player.HP  '''
        self.HP += 50 
        return self.HP

    def use_mana_potion(self):
        '''  This function add 200mana to Player.mana  '''
        self.mana += 200 
        return self.mana