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