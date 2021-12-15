import pytest
import os

from scrypt_test import Character,Player,Enemies, Inventory, bcolors, Shop, Score, Game, Combat


@pytest.fixture
def TestCharacter():
    return Character('Mytest',50,0)

@pytest.fixture
def enemies_test():
    return Enemies('First monster',25,0)

@pytest.fixture
def player_test():
    return Player(3,1,3,250,"test_player",155,8)
    
@pytest.fixture
def combat_test():
    return Combat('combat',50,0,round=1)

@pytest.fixture
def target():
    return 1
@pytest.fixture 
def shop_test():
    return Shop(10,10,10,150)


class TestCharactere:
    def test_init(self, TestCharacter):
        assert TestCharacter.HP == 50
        assert TestCharacter.name == "Mytest"
        assert TestCharacter.is_dead == False
        assert TestCharacter.lvl == 0
        with pytest.raises(ValueError):
            Enemies(10,55,'a')
        with pytest.raises(ValueError):
            Enemies("PlayerTest")
        with pytest.raises(ValueError):
            Enemies("Player",0)


class TestEnemies:
    def test_init(self, enemies_test):
        assert enemies_test.HP == 25 
        assert enemies_test.name == "First monster"
        assert enemies_test.is_dead == False
        with pytest.raises(ValueError):
            Enemies(10,55)
        with pytest.raises(ValueError):
            Enemies("PlayerTest",'15')

    def test_check_hp(self):
        enemies_test_dead = Enemies('First monster',0,0)
        enemies_test_dead.unique().check_hp() 
        assert enemies_test_dead.is_dead == True 
        player_dead = Player(10,10,10,10,'NamePlayer',0,10)
        player_dead.check_hp()
        assert player_dead.is_dead == True

    def test_enemy_attack(self, enemies_test, player_test ):
        assert player_test.HP > enemies_test.enemy_attack(player_test) 
        with pytest.raises(AttributeError):
            player_test.enemy_attack()

    def test_gen(self,enemies_test):
        enemies_group = enemies_test.gen().list_enemies
        assert len(enemies_group) > len(Enemies('MonsterTest',25,0).list_enemies)

    def test_unique(self,enemies_test):
        enemies_group = enemies_test.unique().list_enemies
        assert len(enemies_group) > len(Enemies('MonsterTest',25,0).list_enemies)
        assert enemies_group[0]['HP'] == 25 




class TestPlayer:
    def test_init(self, player_test):
        assert player_test.HP == 155
        assert player_test.name == "test_player"
        assert player_test.is_dead == False
        with pytest.raises(TypeError):
            Player(99,99,0)
        with pytest.raises(TypeError):
            Player("PlayerTest")
        with pytest.raises(TypeError):
            Player("PlayerTest","99",0)
        with pytest.raises(ValueError):
            Player("PlayerTest",99,0,15).use_potion(player_test)
        

    def test_attack_big_punch(self,enemies_test,target, combat_test, player_test):
        
        assert enemies_test.unique().list_enemies[0]['HP'] > player_test.attack_big_punch(enemies_test.unique(),target,combat_test) 
        assert combat_test.round == 2
        with pytest.raises(TypeError):
            player_test.attack_big_punch("51")        
    def test_attack_lightning(self,enemies_test,target,combat_test,player_test):  
        assert enemies_test.unique().list_enemies[0]['HP'] > player_test.attack_lightning(enemies_test, target, combat_test) 
    def test_fire_ball(self,enemies_test,combat_test,player_test):
        assert enemies_test.unique().list_enemies[0]['HP'] > player_test.fire_ball(enemies_test, combat_test) 
    def test_use_potion(self,player_test):
        assert player_test.HP < player_test.use_potion()
    def test_use_maxi_potion(self, player_test):
        assert player_test.HP < player_test.use_maxi_potion() 
        with pytest.raises(TypeError):
            player_test.use_maxi_potion("51") 
    def test_use_mana_potion(self, player_test):
        assert player_test.mana  < player_test.use_mana_potion() 


class Shop:
    def test_def_black_market(self,player_test):
        self.shop_choice = "1"
        assert player_test.potion == 4
        self.shop_choice = "2"
        assert player_test.potion_max == 0
        assert player_test.gold == 200
        self.sell_choice = "1"
        assert player_test.gold == 260
        assert player_test.max_potion == 0

class Game:
    def test_get_enemies(self):
        self.wave = 1 
        assert self.get_enemies(self).list_enemies[0]['Name'] == "First Captain"
