import random
import matplotlib.pyplot as plt
import statistics 


var1 = input("What is the name of the first outcome ")

countVar1 = int(input("Enter your number of the " + var1))

var2 = input("What is the name of the second outcome ")

countVar2 = int(input("Enter your number of the " + var2))

sigValue =float(input("What is the significant probability " ))

numberPicked = int(input("Enter your number picked from the sample : "))

simulationSize = int(input("Enter your number of simulations : "))


allTheEmployees=[]
for i in range(countVar1):    
    allTheEmployees.append(0)


for j in range(countVar2):
    allTheEmployees.append(1)


resultNumber = []
for k in range(numberPicked+1):
    resultNumber.append(k)
print(resultNumber)





counts=[]

def sample():
    end = random.sample(allTheEmployees,numberPicked)
    picked=end.count (1)
    counts.append(picked)
    
    return sample



y=0
while simulationSize>y:
    result= sample()

    y+=1

countsTwo = []

for l in range(numberPicked+1):
    countsTwo.append(counts.count(l))
print(countsTwo)

print(statistics.mean(counts))
print(statistics.stdev(counts))


plt.bar(resultNumber,countsTwo)
plt.title(var2 + ' Selected Distribution')
plt.xlabel('')
plt.ylabel('Count')
plt.show()


