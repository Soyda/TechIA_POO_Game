from dataclasses import dataclass, field
from typing import ClassVar
from abc import ABCMeta, abstractmethod

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

    def check_inventory(self):
        '''This function prints the number of potions available in inventory'''
        print(f"You currently have {self.gold} gold, {self.potion} health potion(s), {self.max_potion} max health potion(s) and {self.mana_potion} mana potion(s) in your inventory.")

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
class Shop():

    pass

