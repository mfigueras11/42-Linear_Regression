import json
import numpy
while 42:
    mileage = input('Enter car mileage(km):')
    if mileage.isnumeric():
        mileage = int(mileage)
        break
        
try:
    with open('theta.json') as f:
        theta = numpy.array(json.load(f))
except:
    theta = numpy.array([0, 0])

price = theta[0] + theta[1] * mileage
print('Your car is worth ' + str(price) + '.')