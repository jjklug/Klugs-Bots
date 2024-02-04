import numpy
import matplotlib.pyplot


backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
targetAngles = numpy.load("data/targetAngles.npy")


#print(backLegSensorValues)

#matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", lw=2)
#matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg", lw=.7)

matplotlib.pyplot.plot(targetAngles, label="Target Angles")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
