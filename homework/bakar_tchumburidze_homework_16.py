
class Student:
    all_students = []
    def __init__(self,name:str,age:int,grade:int):
        assert grade < 4 and grade > 0
        self.name = name
        self.age = age
        self.__grade = grade
        self.subjects_enrolled = []

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
        if len(self.subjects_enrolled) < 3:
            self.subjects_enrolled.append(subject)
            print(f" '{subject}' added to {self.name}'s subjects.")
        else:
            print("sorry, possible only 3 subject")

    def remove_subject(self,subject):
        if subject in self.subjects_enrolled:
            self.subjects_enrolled.remove(subject)
            print(f"'{subject}' removed from {self.name}'s subjects.")
        else:
            print(f"'{subject}' not found in {self.name}'s subjects.")

    def __find_subjects (self):
        subjects = ''
        for subject in self.subjects_enrolled:
            subjects += f'{subject}, '
        subjects = subjects[:-2] + '.'
        return subjects
        
    def display_info(self):
        subjects = self.__find_subjects()
        print(f"name: {self.name}\nAge: {self.age}\nGrade: {self.grade}\nEnroled subjects: {subjects}")
    
    @staticmethod
    def count_students():
        print(f'Number of students: {len(Student.all_students)}')


    @classmethod
    def get_student_by_grade(cls, target_grade):
        print ([student for student in cls.all_students if student.grade == target_grade])
      
                

        


student1 = Student('giorgi','18',1)
student1.add_subject('English')
student1.add_subject('information technology')
student1.add_subject('Matematic')
student1.add_subject('biology') # მეოთხე საგანი არ დაემატება
student1.remove_subject('English') #წაშლა
student2 = Student('levani','18',1)
student3 = Student('gvanca','19',2)
student4 = Student('lika','18',2)
student5 = Student('tornike','18',1)
Student.count_students()   # staticmethod - სტუდენტების საერთო რაოდენობა
Student.get_student_by_grade(2) # classmethod - სტუდენტები კურსის მიხედვით
student1.display_info() # სტუდენტის შესახებ ინფორმაცია. ამ მეთოდში გამოყენებულია ერთი დამალული მეთოდი






