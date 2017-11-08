import random
import math

def getF(x, y):
    return (((4 - (2.1*(x**2)) + ((x**4)/3)) * (x**2)) + (x*y) + ((-4 + (4*(y**2)))* (y**2)))


def getP(dE, t):
    return math.exp((-1*dE)/t)


def getNewRandInRange(x):
    newX = x + random.uniform(-5, 5)
    while (newX > 10) or (newX < -10):
        newX = x + random.uniform(-5, 5)
    return newX

initState1 = random.uniform(-10, 10)
initState2 = random.uniform(-10, 10)

currentState1 = initState1
currentState2 = initState2

BSF = getF(currentState1, currentState2)

T = 1000
Tx = 1 #T minimal

while T > Tx:
    print("T= %f" %T)
    newState1 = getNewRandInRange(currentState1)
    newState2 = getNewRandInRange(currentState2)

    currentF = getF(currentState1, currentState2)
    newF = getF(newState1, newState2)

    print("Current X1= %f" % currentState1)
    print("Current X2= %f" % currentState2)
    print("New X1= %f" % newState1)
    print("New X2= %f" % newState2)
    print("Current F= %f" %currentF)
    print("New F= %f" %newF)
    dE = newF - currentF
    print ("delta E: %f" %dE)

    if (newF < currentF):
        currentState1 = newState1
        currentState2 = newState2
        BSF = getF(newState1, newState2)
    else:
        randNumber = random.uniform(0, 1)
        p = getP(dE, T)
        if (randNumber < p):
            currentState1 = newState1
            currentState2 = newState2

    print("BSF: %f" %BSF)
    print("\n")
    T = T * 0.9

print("Final: %f" %BSF) #final output
