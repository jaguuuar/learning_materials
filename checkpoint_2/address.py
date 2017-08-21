class Address:

    def __init__(self, person, city, street, house_no):
        self.person = person
        self.city = city
        self.street = street
        self.house_no = house_no

    def get_full_address(self):
        full_address = '{}, {}, {} {}'.format(self.person, self.city, self.street, self.house_no)

        return full_address

    def __eq__(self, other):
        return self.__dict__ == other.__dict__



    def __str__(self):
        string = self.person + self.city + self.street + str(self.house_no)
        return string





# adress = Address("Tomasz", "Kraków", "Wrocławska", 12)
# print(adress)
# print(adress.get_full_address())
