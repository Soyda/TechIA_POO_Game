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

    def check_inventory(self,player):
        '''This function prints the number of potions available in inventory'''
        return print(f"\n-----------------------\n Inventory:\n Gold: {player.gold}\n Health potion(s): {player.potion}\n Max health potion(s): {player.max_potion}\n Mana potion(s): {player.mana_potion}\n Gold : {player.gold}\n-----------------------\n")


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
