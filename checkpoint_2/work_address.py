from address import Address

class WorkAddress(Address):

    def __init__(self, person, city, street, house_no, company):
        super().__init__(person, city, street, house_no)
        self.company = company

    def get_full_address(self):
        full_address = '{}, {}, {} {}, {}'.format(self.person, self.city, self.street, self.house_no, self.company)

        return full_address


# work_address = WorkAddress("Kamil", "Kraków", "Łokietka", 17, "CodeCool")
# print(work_address.get_full_address())
