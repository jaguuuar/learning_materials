from character import Character
from item import Item
from inventory import Inventory

class Hero:

    def __init__(self, character, inventory, experience, level):
        self.character = character
        self.inventory = inventory
        self.experience = experience
        self.level = level
