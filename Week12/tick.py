# Tick class for aggregation
class Tick:
    def __init__(self):
        print("Aggregation: Tick is created.")

    def suck_blood(self):
        print("Tick is feeding...")

    def __del__(self):
        print("Aggregation: Tick is destroyed.")