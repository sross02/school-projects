import random

def roll_die():
    return random.randint(1, 6)

def roll_until_six():
    roll_count = 0
    roll = roll_die()
    while roll != 6:
        roll_count += 1
        roll = roll_die()
    return roll_count

trialNum = 0
total_rolls = 0
while trialNum < 100:
    total_rolls += roll_until_six()
    trialNum += 1

average_rolls = total_rolls / trialNum
print("Total rolls:", total_rolls)
print("Number of Trials:", trialNum)
print("Average Number of Rolls to get roll a six:", average_rolls)
