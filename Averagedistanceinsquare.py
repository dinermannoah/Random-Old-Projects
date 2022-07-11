import random
import math
import collections

xsize = 14
ysize = 11
ds = [0]
def distance():
    x1 = random.uniform (0,xsize)
    x2 = random.uniform (0,xsize)
    xd = x1-x2
    sx= xd*xd
    y1 = random.uniform (0,ysize)
    y2 = random.uniform (0,ysize)
    yd = y1-y2
    sy = yd*yd
    s = sy+sx
    dis = math.sqrt(s)
    ds.append(dis)
    return dis
   
x=0

while x<10000:
    result = distance()
    x+=1

res2 = sum(ds)/len(ds)
print (res2)






