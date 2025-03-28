from mammal import Mammal

class Puma(Mammal):
    def __init__(self, p_age, tick):
        print("Constructor: Inside the Child class constructor: Adding the Puma parts of a puma")
        # Call the parent constructor
        super().__init__(p_age)

        # Aggregation: store tick reference
        self.tick = tick

        # Puma-specific fields
        self.sharp_claws = True

    def __del__(self):
        print("Destructor: The garbage collector is now deleting the Puma part of the object")
        super(Puma, self).__del__()
