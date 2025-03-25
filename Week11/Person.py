# Lab 11 - Create the Person class
class Person:
    # Constructor
    def __init__(self, p_name, p_age, p_height):
        print("Constructing the person object")
        self.__name = p_name
        self.__age = p_age
        self.__height = p_height
        self.public_prop = "I'm public"

    # Getter for name: version 1
    @property
    def name(self):
        return self.__name

    # Setter for name: version 1
    @name.setter
    def name(self, new_name):
       self.__name = new_name

    # ----------------------------------

    # Getter for name: version 2
    # def get_name(self):
    #    return self.__name

    # Setter for name: version 2
    #def set_name(self, new_name):
    #    self.__name = new_name

    def __del__(self):
        print("The garbage collector is automatically destroying the person object")

person1 = Person("Mark", 20, 6)

# version 1
print("The name of the person is: " + str(person1.name))
person1.name = "Alfred"
print("The name of the person is: " + str(person1.name))
print("public: " + str(person1.public_prop))
# print("private: " + str(person1.__name)) # Cause an Error
# print("private: " + str(person1._Person__name)) 


# version 2
#print("The name of the person is: " + str(person1.get_name()))
#person1.set_name("Alfred")
#print("The name of the person is: " + str(person1.get_name()))
