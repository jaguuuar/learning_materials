
class Item:


    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
