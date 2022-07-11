
import random

rolls = []
def roll2Dice():
    roll1 = random.randint (1,6)
    roll2 = random.randint (1,6)
    roll = roll1+roll2
    rolls.append(roll)
    return roll
   
x=0

while x<100:
    result = roll2Dice()
    print (result)
    print (rolls)
    x+=1

print(rolls.count(5))
