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
        return print(f"Inventory:\n Gold: {self.gold}\n Health potion(s): {self.potion}\n Max health potion(s): {self.max_potion}\n Mana potion(s): {self.mana_potion}\n")

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
class Shop(Inventory):
    inventory : Inventory
    potion_stock : int = 5
    max_potion_stock : int = 2
    mana_potion_stock : int = 3
    gold_stock : int = 200
    shop_choice : str = field(init=False)
    sell_choice : str = field(init=False)
    leave : bool = True
    leave_sell : bool = True

    def display_shop(self):
        while(self.leave):
            print('\nWelcome to the shop, feel free to spend all your gold here !')
            print(f"1. Buy a health potion for 20 gold. {self.potion_stock} in stock")
            print(f"2. Buy a max health potion 50 gold. {self.max_potion_stock} in stock")
            print(f"3. Buy a mana potion 30 gold. {self.mana_potion_stock} in stock")
            print(f"4. Sell an item.")
            print("5. Leave shop.\n")
            self.shop_choice = input("What is your choice ?\n")

            if self.shop_choice == '1':
                if self.potion_stock > 0 and self.gold >= 20:
                    self.potion_stock -= 1
                    self.potion += 1
                    self.gold -= 20
                    self.gold_stock += 20
                    print("A health potion has been added to your inventory.\n")
                else :
                    print("Sorry, you can't buy this item for the moment.\n")
            elif self.shop_choice == '2':
                if self.max_potion_stock > 0 and self.gold >= 50:
                    self.max_potion_stock -= 1
                    self.max_potion += 1
                    self.gold -= 50
                    self.gold_stock += 50
                    print("A max health potion has been added to your inventory.\n")
                else :
                    print("Sorry, you can't buy this item for the moment.\n")
            elif self.shop_choice == '3':
                if self.mana_potion_stock > 0 and self.gold >= 30:
                    self.mana_potion_stock -= 1
                    self.mana_potion += 1
                    self.gold -= 30
                    self.gold_stock += 30
                    print("A mana health potion has been added to your inventory.\n")
                else :
                    print("Sorry, you can't buy this item for the moment.\n")
            elif self.shop_choice == '4':
                while(self.leave_sell):
                    # self.check_inventory()
                    print(f"\nShop has {self.gold_stock} gold.\n")
                    print(f"1. Sell a health potion for 10 gold.")
                    print(f"2. Sell a max health potion 25 gold.")
                    print(f"3. Sell a mana potion 15 gold.")
                    print(f"4. Back to shop.\n")
                    self.sell_choice = input("What is your choice ?\n")

                    if self.sell_choice == '1':
                        if self.potion > 0 and self.gold_stock >= 10:
                            self.potion_stock += 1
                            self.potion -= 1
                            self.gold += 10
                            self.gold_stock -= 10
                            print("You got 10 gold.\n")
                        else :
                            print("Sorry, we can't buy this item for the moment.\n")
                    elif self.sell_choice == '2':
                        if self.potion > 0 and self.gold_stock >= 25:
                            self.potion_stock += 1
                            self.potion -= 1
                            self.gold += 25
                            self.gold_stock -= 25
                            print("You got 25 gold.\n")
                        else :
                            print("Sorry, we can't buy this item for the moment.\n")
                    elif self.sell_choice == '3':
                        if self.potion > 0 and self.gold_stock >= 15:
                            self.potion_stock += 1
                            self.potion -= 1
                            self.gold += 15
                            self.gold_stock -= 15
                            print("You got 15 gold.\n")
                        else :
                            print("Sorry, we can't buy this item for the moment.\n")
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
# shop.display_shop(shop)

