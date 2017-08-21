from teacher import Teacher
from student import Student

class Class:

    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []


    def get_best_student(self):
        best_grade = max(student.get_average_grade() for student in self.students)
        best_student = [student for student in self.students if student.get_average_grade() == best_grade][0]

        return best_student

    def get_average_grade(self):
        all_grades = [student.get_average_grade() for student in self.students]
        average_grade = sum(all_grades) / len(all_grades)

        return average_grade


    def get_class_subjects(self):
        class_subjects = []

        for teacher in self.teachers:
            for subject in teacher.subjects:
                class_subjects.append(subject)

        return class_subjects


    def sort_students(self, attr):

        is_sorted = False
        while not is_sorted:
            is_sorted = False

            for i in range(len(self.students)):
                for j in range(i+1, len(self.students)):
                    if attr == "alph":
                        student = self.students[i].last_name
                        next_student = self.students[j].last_name

                    elif attr == "grade":
                        next_student = self.students[i].get_average_grade()
                        student = self.students[j].get_average_grade()

                    if next_student < student:
                        self.students[j], self.students[i] = self.students[i], self.students[j]
                        is_sorted = True



# class1 = Class("1C")
#
# student1 = Student("Marcin", "Solak")
# student1.grades = [4, 5, 2, 3]
#
# student2 = Student("Tomek", "Pipka")
# student2.grades = [4, 3, 3, 2]
#
# student3 = Student("Marek", "Cyc")
# student3.grades = [4, 3, 5, 6]
#
# teacher1 = Teacher("Brigia", "Wonsz")
# teacher2 = Teacher("Maria", "Wrona")
#
# teacher1.subjects = ["Polski", "WOS"]
# teacher2.subjects = ["Matma", "Fiza", "Infa"]
#
#
# class1.students = [student1, student2, student3]
# class1.teachers = [teacher1, teacher2]

# best_student = class1.get_best_student()
# print(best_student.get_full_name())
#
# aver = class1.get_average_grade()
# print(aver)
#
# sub = class1.get_class_subjects()
# print(sub)
#
# class1.sort_students("alph")
#
# for student in class1.students:
#     print(student.get_full_name(), student.get_average_grade())
