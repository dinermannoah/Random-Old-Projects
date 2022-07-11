import random

wins=[]
def play():
    number1 = random.randint (1,50)
    number2 = random.randint (1,49)
    number3 = random.randint (1,48)
    number4 = random.randint (1,47)
    number5 = random.randint (1,46)
    realnumber = number1+number2+number3+number4+number5
    if realnumber <= 10:
        wins.append(realnumber)
    return play
x=0

while x<100000000:
    result = play()
    
    x+=1
        
print (wins.count(5))
print (wins)  








