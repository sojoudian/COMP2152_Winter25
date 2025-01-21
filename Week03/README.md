
# Problem: Fantasy Dice Battle Arena

You're tasked with creating a simple text-based battle simulation game using Python. In this game:

### Dice Options
Use `list()` and `range()` to create a list of dice values (`[1, 2, 3, 4, 5, 6]`). These dice will determine the strength of the hero and the monster in battle.

### Weapons Array
You have a list of weapons with increasing strength: `['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']`.

### Iterating Weapons
Use a `for` loop with the `in` keyword to iterate over the weapons array and display the available weapons to the player.

### Player Input Validation
Ask the player to input an integer between 1 and 6 for their combat strength (`combatStrength`) and monster combat strength (`mCombatStrength`). Validate the input to ensure it's an integer between 1 and 6. If the input is invalid, prompt the user again.

### Battle Sequence
Simulate 20 rounds of battle using a `for` loop with a range from 1 to 20, stepping by 2. Each round:

1. Roll a dice for the hero and the monster (use `random.choice(diceOptions)`).
2. Add the dice roll to `combatStrength` and `mCombatStrength`.
3. Announce the selected weapon based on the dice roll.
4. Determine the winner of the round (higher combat strength wins).
5. Print the battle details (e.g., round number, selected weapon, hero strength, monster strength, and winner).

### Break Condition
If the current round number (`j`) is 11, announce a sudden "Battle Truce" and break out of the loop.

---

### Expected Output Example:

```
Available Weapons:
1. Fist
2. Knife
3. Club
4. Gun
5. Bomb
6. Nuclear Bomb

Enter your combat strength (1-6): 3
Enter monster's combat strength (1-6): 5

Round 1: Hero rolled 4, Monster rolled 6.
Hero selected: Knife, Monster selected: Bomb.
Hero Total Strength: 7, Monster Total Strength: 11.
Monster wins the round!

Round 3: Hero rolled 6, Monster rolled 2.
Hero selected: Nuclear Bomb, Monster selected: Club.
Hero Total Strength: 9, Monster Total Strength: 7.
Hero wins the round!

...
Battle Truce declared in Round 11. Game Over!
```

---

This problem combines the original learning goals with an engaging scenario, encouraging students to use creativity and problem-solving skills. It covers:

- `list()` and `range()`

- Loops with `in` and `range()`

- Input validation

- Conditional statements

- Break statements in loops

---

# Starter Code:

```python
import random

# Setup
diceOptions = list(range(1, 7))
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']
print("Available Weapons:", ', '.join(weapons))

# Inputs
combatStrength = max(1, min(6, int(input("Hero strength (1-6): "))))
mCombatStrength = max(1, min(6, int(input("Monster strength (1-6): "))))

# Battle
for j in range(1, 21, 2):
    heroRoll, monsterRoll = random.choice(diceOptions), random.choice(diceOptions)
    heroTotal, monsterTotal = combatStrength + heroRoll, mCombatStrength + monsterRoll
    print(f"Round {j}: Hero({weapons[heroRoll - 1]})={heroTotal}, Monster({weapons[monsterRoll - 1]})={monsterTotal}.", 
          "Hero wins!" if heroTotal > monsterTotal else "Monster wins!" if heroTotal < monsterTotal else "Tie!")
    if j == 11:
        print("Battle Truce declared. Game Over!")
        break

```
