
class Teacher:


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.subjects = []


    def get_full_name(self):
        full_address = '{} {}'.format(self.first_name, self.last_name)
        return full_address


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
