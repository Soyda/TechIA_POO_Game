import pytest
import os

from class_entity import Enemies, Character, Player 


@pytest.fixture
def TestCharacter():
    return Character('Mytest',50,0)

@pytest.fixture
def enemies_test():
    return Enemies('First monster',25,0)


@pytest.fixture
def player_test():
    return Player('TestPlayer',50,0)



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
        assert enemies_test_dead.unique().check_hp() == f"{enemies_test_dead.list_enemies[0]['Name']} is dead"

    def test_enemy_attack(x, enemies_test):
        x = 20 
        assert enemies_test.enemy_attack(x) <= 16 and enemies_test.enemy_attack(x) >= 11
        x = "20"
        with pytest.raises(TypeError):
            enemies_test.enemy_attack(x)

    def test_gen(self,enemies_test):
        enemies_group = enemies_test.gen().list_enemies
        assert len(enemies_group) > len(Enemies('MonsterTest',25,0).list_enemies)

    def test_unique(self,enemies_test):
        enemies_group = enemies_test.unique().list_enemies
        assert len(enemies_group) > len(Enemies('MonsterTest',25,0).list_enemies)
        assert enemies_group[0]['HP'] == 25 


class TestPlayer:
    def test_init(self, player_test):
        assert player_test.HP == 50 
        assert player_test.name == "TestPlayer"
        assert player_test.is_dead == False
        with pytest.raises(ValueError):
            Player(99,99)
        with pytest.raises(ValueError):
            Player("PlayerTest")
        with pytest.raises(ValueError):
            Player("PlayerTest","99",0)
        with pytest.raises(AttributeError):
            Player("PlayerTest",99,0).use_potion(51)
        

    def test_attack_big_punch(self,enemies_test,player_test):
        assert player_test.attack_big_punch(enemies_test.unique().list_enemies[0]['HP']) < enemies_test.unique().list_enemies[0]['HP']
        with pytest.raises(TypeError):
            player_test.attack_big_punch("51")        
    def test_attack_lightning(self,enemies_test,player_test):  
        assert player_test.attack_lightning(enemies_test.unique().list_enemies[0]['HP']) < enemies_test.unique().list_enemies[0]['HP']
    def test_fire_ball(self,enemies_test,player_test):
        assert player_test.fire_ball(enemies_test.unique().list_enemies[0]['HP']) < enemies_test.unique().list_enemies[0]['HP']
    def test_use_potion(self,player_test):
        assert player_test.use_potion(player_test) > player_test.HP
    def test_use_maxi_potion(self, player_test):
        assert player_test.use_maxi_potion(player_test) > player_test.HP
        with pytest.raises(AttributeError):
            player_test.use_maxi_potion("51") 
    def test_use_mana_potion(self, player_test):
        assert player_test.use_mana_potion(player_test) > player_test.mana