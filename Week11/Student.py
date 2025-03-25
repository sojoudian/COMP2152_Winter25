# Define the Student class inheriting from Person
class Student(Person):
    def __init__(self, p_name, p_age, p_height, p_major):
        # Call the constructor of the parent (Person) class
        super().__init__(p_name, p_age, p_height)
        # Set the new public property
        self.major = p_major
        # Print statement to confirm creation of a Student object
        print("This time it's a Student object")

# Create an instance of Student
student1 = Student("Maria", 22, 6, "Computer Science")

# Access inherited and new attributes
print("Student's name (inherited via magic getter):", student1.name)
print("Student's major (new public property):", student1.major)
