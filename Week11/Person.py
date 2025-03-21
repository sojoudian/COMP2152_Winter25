class Person():
    def __init__(self, p_name, p_age, p_height):
        self.__name = p_name
        self.__age = p_age
        self.__height = p_height
        self.public_prop = "I'm public"

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __del__(self):
        print("The garbage collector is automatically destroying the person object")        

person1 = Person("Mike", 20, 6)
print("the name of the person is: " + str(person1.name))

person1.name = "Alfred"
print("the name of the person is: " + str(person1.name))