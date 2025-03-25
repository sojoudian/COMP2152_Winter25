# Heart class for composition
class Heart:
    def __init__(self):
        print("Composition: Heart is created.")
        self.beats_per_minute = 72
    
    def beat(self):
        print("Heart is beating...")
    
    def __del__(self):
        print("Composition: Heart is destroyed.")