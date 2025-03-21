from Person import Person

class Student(Person):
    def __init__(self, p_name, p_age, p_height, p_major):
        super().__init__(p_name, p_age, p_height)
        self.major = p_major
        print("This time it's a Student Object")

student1 = Student("Mark", 22, 6, "Computer Science")
print("The student name is: " + str(student1.name))
print("The student major is: " + str(student1.major))

    