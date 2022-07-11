import math
num1 = 0
num2 = 1
n = 1
fib = []
gr = []
fib.append(num1)
fib.append(num2)

for i in range (39):
    newNum = fib[n] + fib[n-1]
    fib.append(newNum)
    n+=1
    ratio = fib[n] / fib[n-1]
    gr.append(ratio)

m = (1+ math.sqrt(5))/2
print (fib)
print(gr[n-2])
print (m)
print (gr[n-2]-m)





