from mammal import Mammal

# Lab 12 - Child can inherit only public fields from the parent
class Person(Mammal):
    # fields from Parent
    # age

    # fields
    # name
    # __height

    def __init__(self, p_name, p_age, p_height):
        # Lab 12 - Call the parent class constructor

        # Set the Person-specific fields
        print("Constructor: Adding the Person parts of a person")


    def __del__(self):
        print("Destructor: The garbage collector is now deleting the person object")
        

        # Complex getter for height

    # Complex setter for height


    # Lab 12 - Private or protected METHODS are not possible in python.
    # Lab 12 - This means that all methods are public and can be overridden in a derived class.
    def love(self):
        print("This human is feeling love in a more complex emotional way...")
