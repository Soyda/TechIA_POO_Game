from abc import abstractmethod, ABCMeta
from dataclasses import dataclass 
from class_package.entity import Enemies
from class_package.colors import bcolors
from class_package.inventory import Shop

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