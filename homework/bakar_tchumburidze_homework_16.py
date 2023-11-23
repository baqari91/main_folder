
class Student:
    subjects_enrolled = []
    all_students = []
    def __init__(self,name:str,age:int,grade:int):
        assert grade < 4 and grade > 0
        self.name = name
        self.age = age
        self.__grade = grade

        Student.all_students.append(self)
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.age},{self.__grade})"

    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self,value):
        assert value < 4 and value > 0
        self.__grade = value
    
    def add_subject(self,subject):
        self.subjects_enrolled.append(subject)
        print(f"{subject} added to {self.name}'s subjects.")

    def remove_subject(self,subject):
        if subject in self.subjects_enrolled:
            self.subjects_enrolled.remove(subject)
            print(f"{subject} removed from {self.name}'s subjects.")
        else:
            print(f"{subject} not found in {self.name}'s subjects.")
    def calculate_gpa(self,s):
        pass
    def display_info(self):
        subjects = ''
        for i in self.subjects_enrolled:
            subjects+=f'{i}, ' 
        subjects = subjects[:-2] + '.'
        print(f"name: {self.name}\nAge: {self.age}\nGrade: {self.grade}\nEnroled subjects: {subjects}")
    
    @staticmethod
    def count_students():
        print(f'Number of students: {len(Student.all_students)}')

    @classmethod
    def get_student_by_grade(cls, target_grade):
        return [student for student in cls.all_students if Student.grade == target_grade ]

student1 = Student('giorgi','18',2)
student1.add_subject('English')
student1.add_subject('rame')
student1.add_subject('Matematic')
student1.remove_subject('rame')
student1.display_info()
student1.grade = 1
student1.display_info()

student2 = Student('malxazi','17',1)
student2.add_subject('English')
student2.add_subject('rame')
student2.add_subject('Matematic')

print(Student.all_students)
Student.count_students()
print (Student.get_student_by_grade(1))
print(Student.grade)
student2.display_info()