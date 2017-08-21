

class Student:


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []


    def get_full_name(self):
        full_address = '{} {}'.format(self.first_name, self.last_name)
        return full_address


    def __eq__(self, other):
        return self.__dict__ == other.__dict__


    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.grades)
        return average_grade



# student1 = Student("Marcin", "Solak")
# print(student1.first_name)
#
# student1.grades = [4, 5, 3, 3]
# print(student1.get_average_grade())
