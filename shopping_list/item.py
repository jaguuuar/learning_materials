
class Item:

    def __init__(self, name, quantity, unit, price_per_unit, categories, is_bought = False):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.price_per_unit = price_per_unit
        self.categories = categories
        self.is_bought = is_bought


    def __str__(self):
        if self.is_bought:
            bought = "Yes"
        else:
            bought = "NO"

        string = "{}, {} {}, {}, {}, {}".format(self.name, self.quantity, self.unit, self.price_per_unit,
                                                self.categories, bought)

        return string


    def get_total_price(self):
        


item1 = Item("Ser biały", 0.25, "kilogram", 10, "nabiał")

print(item1)
