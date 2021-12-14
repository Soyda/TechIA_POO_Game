from abc import abstractmethod, ABCMeta
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
            return f"{str(count) + ' player is dead' if count == 1 else str(count) + ' players are dead' }" 
        if len(self.list_enemies) == count:
            self.status = False 
        if self.HP <= 0 :
            self.health_status = False 
            self.is_dead = True 
            return f'You are dead.. Try again {self.name}'