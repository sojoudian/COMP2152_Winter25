class Person:
    # Constructor
    def __init__(self, p_name, p_age, p_height):
        print("Constructing the person object")
        self.__name = p_name
        self.__age = p_age
        self.__height = p_height
        self.public_prop = "I'm Public"

        # Getter for name
        @property
        def name(self):
            return self.__name
        
        # Setter for name
        @name.setter
        def name(self, new_name):
            self.__name = new_name
        
        def __del__(self):
            print("The grabage collector is automatically destroying the person object")