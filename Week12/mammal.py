from heart import Heart

class Mammal:
    def __init__(self, p_age, tick=None):  # Aggregation through parameter
        print("Constructor: Inside the Parent class constructor: Making the Mammal part of the object")
        self.age = p_age
        self.__live_birth = True

        self.heart = Heart()
        # Tick is an external, may or may not exist
        self.tick= tick



    def __del__(self):
        print("Destructor: The garbage collector is now deleting the Mammal part of the object")

    @property
    def live_birth(self):
        self.__live_birth
    @live_birth.setter
    def live_birth(self, p_live_birth):
        self.__live_birth = p_live_birth

    def love(self):
        print("This mammal is feeling love..")

    def mammal_chechup(self):
        self.heart.beat()
        if self.tick:
            self.tick.consume_blood()

    def __str__(self):
        tick_status = "attached" if self.tick else "none"
        return f"Mammal(age={self.age}, live_birth={self.__live_birth}, tick={tick_status}, heart_bpm={self.heart.bpm})"
