from item import Item

class Inventory:


    def __init__(self, capacity=6, max_weight=15):
        self.capacity = capacity
        self.max_weight = max_weight
        self.items = []


    def get_inventory_size(self):
        return len(self.items)


    def get_inventory_weight(self):
        inventory_weight = 0
        for item in self.items:
            inventory_weight += item.weight

        return inventory_weight


    def get_the_heaviest_item(self):
        max_weight = max(item.weight for item in self.items)
        heaviest_item = [item for item in self.items if item.weight == max_weight][0]

        return heaviest_item


    def add_item(self, item):
        if self.get_inventory_weight() + item.weight > self.max_weight:
            print("You are to heavy!")

        elif self.get_inventory_size() + 1 > self.capacity:
            print("To many items in inventory!")

        else:
            self.items.append(item)


    def drop_item(self, drop_item):
        items = []
        for item in self.items:
            if item != drop_item:
                items.append(item)

        self.items = items



'''
item1 = Item("miecz", "zardzewiały sztylet", 4)
item2 = Item("runa", "ukryta w niej moc", 1)
item3 = Item("głowa orka", "smierdzaca jak dupa", 3)
item4 = Item("łopata", "piękny szpadel", 3)
item5 = Item("apteczka", "metykamenty szpitalne", 2)
item6 = Item("kilof", "do kopania diaxów", 5)
item7 = Item("strzały", "stare patyki", 1)
item8 = Item("miecz", "zardzewiały sztylet", 4)

inventory = Inventory()
inventory.items = [item1, item2, item3]

inventory.add_item(item4)
inventory.add_item(item5)
inventory.add_item(item6)
inventory.add_item(item7)

print("inventory size:", inventory.get_inventory_size())
print("inventory weight:", inventory.get_inventory_weight())
print("heaviest item:", inventory.get_the_heaviest_item().name)
print()

inventory.drop_item(item1)
print("inventory size:", inventory.get_inventory_size())
print("inventory weight:", inventory.get_inventory_weight())
print("heaviest item:", inventory.get_the_heaviest_item().name)

print()
for item in inventory.items:
    print(item.name, end = ", ")

'''
