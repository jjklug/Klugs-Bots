#import constants as c
#import time
#import numpy
#import random
from simulation import SIMULATION

simulation = SIMULATION()

simulation.Run()

#sensor and motor value arrays created below

#targetAngles = numpy.linspace(0, 2*int(numpy.pi), 999)
#backleg_targetAngles = (c.backleg_amplitude)*numpy.sin(c.backleg_frequency*targetAngles+c.backleg_phaseOffset)
#frontleg_targetAngles = (c.frontleg_amplitude)*numpy.sin(c.frontleg_frequency*targetAngles+c.frontleg_phaseOffset)





#saving for analyze.py
#numpy.save("data/backleg_targetAngles.npy", backleg_targetAngles)
#numpy.save("data/frontleg_targetAngles.npy", frontleg_targetAngles)
#exit()


#saving data to files
#numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
#numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
