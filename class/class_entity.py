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
        for i in self.list_enemies : 
            if i['HP'] <= 0 :
                i['HP'] = 0 
                i['is_dead'] = True 
            print( f"{i['Name']} is dead")

            


@dataclass
class Enemies(Character):
    list_enemies : list = field(default_factory=list)

    @staticmethod
    def enemy_attack(x):
        ''' Function for enemy attack   
        ---------------  
        x should be an int  (Like x = Player.HP) '''
        return x - randint(4,9)  
    def gen(self):
        ''' Function to create and add random enemies
         add this instance and this enemies into a list
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
        ''' Function to crate and add only this instance into the "list_enemies"
        ---------------  
        '''
        self.list_enemies.append({"Name" : self.name , "HP" : self.HP, 'Level' : self.lvl , 'is_dead' : self.is_dead})
        return self




@dataclass
class Player(Character):

    @staticmethod
    def attack_big_punch(x) : 
        ''' Function to attack enemy by random between 5 and 10   
        ---------------  
        x should be an int  (Like x = enemy_HP) '''
        x -= randint(5,10)
        return x  

    @staticmethod
    def attack_lightning(x):
        ''' Function to attack group of enemy by random damages between 8 and 16
        ---------------  
        x should be an int  (Like x = enemy_HP)   '''
        return x - randint(8,16)

    @staticmethod
    def fire_ball(x):
        return x - randint(8,16)

    @staticmethod
    def use_potion(self):
        '''  This function add 15HP to HP_player 
        ---------------  
        x should be instance of class (Like x = player_hp)  '''
        return self.HP + 15

    @staticmethod
    def use_maxi_potion(self):
        '''  This function add 50HP to HP_player 
        ---------------  
        x should be an int  (Like x = player_hp)  '''
        return self.HP + 50