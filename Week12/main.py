from mammal import Mammal
from person import Person
from mammal import Mammal
from puma import Puma
from tick import Tick
from heart import Heart

print("--- Creating just a mammal object --- ")
just_mammal = Mammal(5)
print("The age of this specific mammal is: " + str(just_mammal.age))
just_mammal.love()  # Base method
print("Do mammals give live birth: " + str(just_mammal.live_birth))

print("\n--- Creating a Person object (composition with Heart) --- ")
person1 = Person("Mark", 20, 5)
print("Name is: " + str(person1.name))
print("Age is: " + str(person1.age))
print("Height is: " + str(person1.height))

# Accessing heart through composition
print("Heart rate: " + str(person1.heart.beats_per_minute))
person1.heart.beat()
person1.age = 25
print(str(person1.name) + "'s new age is: " + str(person1.age))

# Polymorphism: overridden method
person1.love()
print("Do humans give live birth: " + str(person1.live_birth))

print("\n--- Creating a Tick object for aggregation --- ")
tick1 = Tick()
tick1.suck_blood()

print("\n--- Creating a Puma object (aggregation with Tick) --- ")
puma1 = Puma(2, tick1)
print("Puma's age is: " + str(puma1.age))
print("Puma has sharp claws: " + str(puma1.sharp_claws))

# Polymorphism: overridden method
puma1.love()

# Aggregated object interaction
puma1.tick.suck_blood()

# Optional: show that tail_length is not defined if not implemented
# print(puma1.tail_length)  # Uncomment only if tail_length exists

print("--- Destructions due to end of the scope ---")