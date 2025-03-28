from heart import Heart

class Mammal:
    def __init__():  # Aggregation through parameter
        print("Constructor: Inside the Parent class constructor: Making the Mammal part of the object")

    def __del__(self):
        print("Destructor: The garbage collector is now deleting the Mammal part of the object")



    def __str__(self):
        tick_status = "attached" if self.tick else "none"
        return f"Mammal(age={self.age}, live_birth={self.__live_birth}, tick={tick_status}, heart_bpm={self.heart.bpm})"
