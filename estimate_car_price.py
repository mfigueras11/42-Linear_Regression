import json
import numpy
numpy.set_printoptions(precision=2)
while 42:
    mileage = input('Enter car mileage(km):')
    if mileage.isnumeric():
        mileage = int(mileage)
        break
        
try:
    with open('theta.json') as f:
        data = json.load(f)
        theta = numpy.array(data[0])
        mu = data[1]
        std = data[2]
except:
    theta = numpy.array([0, 0])
    mu = 0
    std = 0
mileage = (mileage - mu) / std
price = int(numpy.around(theta[0][0] + theta[1][0] * mileage))
print('Your car is worth ' + str(price) + '€.')