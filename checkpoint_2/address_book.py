from address import Address
from work_address import WorkAddress
import csv

class AddressBook:

    def __init__(self, name):
        self.name = name
        self.addresses = []


    def add_address(self, address):
        if isinstance(address, Address):
            self.addresses.append(address)

        else:
            raise TypeError


    def find(self, search_phrase):
        matching_objects = []

        for address in self.addresses:
            full_address = address.get_full_address()

            if search_phrase.lower() in full_address.lower():
                matching_objects.append(address)

        return matching_objects


    def sort(self):

        is_sorted = False
        while not is_sorted:
            is_sorted = False

            for i in range(len(self.addresses)):
                for j in range(i+1, len(self.addresses)):
                    if self.addresses[j].get_full_address() < self.addresses[i].get_full_address():
                        self.addresses[j], self.addresses[i] = self.addresses[i], self.addresses[j]
                        is_sorted = True


    @classmethod
    def create_from_csv(cls, list_name, csv_path):
        new_book = cls(list_name)

        with open(csv_path) as csvfile:
            addresses_csv = csv.reader(csvfile, delimiter = ',')
            next(csvfile)
            for address in addresses_csv:
                person = address[0]
                city = address[1]
                street = address[2]
                house_no = address[3]
                company = address[4]

                if company == '':
                    new_address = Address(person, city, street, house_no)

                else:
                    new_address = WorkAddress(person, city, street, house_no, company)

                new_book.add_address(new_address)

        return new_book


    def save_to_csv(self):
        with open("book_name.csv", "w") as file:
            file.write("person,city,street,house_no,company\n")

            for address in self.addresses:
                if "company" in address.__dict__.keys():
                    strig_address = '{},{},{},{},{}'.format(address.person, address.city, address.street,
                                                            address.house_no, address.company)

                else:
                    strig_address = '{},{},{},{},'.format(address.person, address.city, address.street, address.house_no)

                file.write(strig_address + "\n")









# book = AddressBook("dupa")
#
# adress = Address("Tomasz", "Kraków", "Wrocławska", 12)
# work_address = WorkAddress("Kamil", "Kraków", "Łokietka", 17, "CodeCool")
#
# print(work_address.__dict__.keys())
#
# book.add_address(adress)
# book.add_address(work_address)
#
# book.sort()
#
# for element in book.addresses:
#     print(element.get_full_address())
#
# print()
# bookie = AddressBook.create_from_csv("buczka", "addresses.csv")
#
# for element in bookie.addresses:
#     print(element.get_full_address())
#
# bookie.save_to_csv()
