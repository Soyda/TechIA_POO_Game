import pytest
import os
from class_inventory import Inventory

@pytest.fixture
def inventory_test():
   return Inventory(10, 2, 3, 100)

class TestInventory():
    def test_init(self, inventory_test):
        assert inventory_test.potion == 10
        assert type(inventory_test.potion) == int
        assert inventory_test.max_potion == 2
        assert type(inventory_test.max_potion) == int
        assert inventory_test.mana_potion == 3
        assert type(inventory_test.mana_potion) == int
        assert inventory_test.gold == 100
        assert type(inventory_test.gold) == int
    
    def test_add_potion(self, inventory_test) :
        inventory_test.add_potion()
        assert inventory_test.potion == 11
    
    def test_add_max_potion(self, inventory_test) :
        inventory_test.add_max_potion()
        assert inventory_test.max_potion == 3
    
    def test_add_mana_potion(self, inventory_test) :
        inventory_test.add_mana_potion()
        assert inventory_test.mana_potion == 4
    
    def test_add_gold(self, inventory_test) :
        inventory_test.add_gold(150)
        assert inventory_test.gold == 250
    
    def test_remove_potion(self, inventory_test):
        inventory_test.remove_potion()
        assert inventory_test.potion == 9
    
    def test_remove_max_potion(self, inventory_test):
        inventory_test.remove_max_potion()
        assert inventory_test.max_potion == 1

    def test_remove_mana_potion(self, inventory_test):
        inventory_test.remove_mana_potion()
        assert inventory_test.mana_potion == 2
    
    def test_remove_gold(self, inventory_test):
        inventory_test.remove_gold(75)
        assert inventory_test.gold == 25

