import collections
import random

rolls = []
def roll3Dice():
    roll1 = random.randint (1,6)
    roll2 = random.randint (1,6)
    roll3 = random.randint (1,6)
    roll = roll1+roll2+roll3
    rolls.append(roll)
    return roll
   
x=0

while x<10000:
    result = roll3Dice()

    x+=1

print(rolls.count(5))
print ('threes')
print (rolls.count(3))
print ('fours')
print (rolls.count(4))
print ('fives')
print (rolls.count(5))
print ('sixes')
print (rolls.count(6))
print ('sevens')
print (rolls.count(7))
print ('eights')
print (rolls.count(8))
print ('nines')
print (rolls.count(9))
print ('tens')
print (rolls.count(10))
print ('elevens')
print (rolls.count(11))
print ('twelves')
print (rolls.count(12))
print ('thirteens')
print (rolls.count(13))
print ('fourteens')
print (rolls.count(14))
print ('fifteens')
print (rolls.count(15))
print ('sixteens')
print (rolls.count(16))
print ('seventeens')
print (rolls.count(17))
print ('eighteens')
print (rolls.count(18))
