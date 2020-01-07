"""
This problem was asked by Google.
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x2 + y2 = r2.

"""
import random
#using r = 1
interval=10000000
insideCircle=0
outsideCircle=0
for i in range(interval):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    distFromOrig = x**2 + y**2 
    #since r^2 = x^2 + y^2
    if distFromOrig <= 1:
        insideCircle = insideCircle + 1
    else:
        outsideCircle = outsideCircle + 1

#area of circle/ area of square = π  r^2/ 2r*2r =
pi = 4* insideCircle/ (insideCircle + outsideCircle)
print(pi)
