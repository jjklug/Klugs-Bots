import numpy
import matplotlib.pyplot


backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
backleg_targetAngles = numpy.load("data/backleg_targetAngles.npy")
frontleg_targetAngles = numpy.load("data/frontleg_targetAngles.npy")

#print(backLegSensorValues)

#matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", lw=2)
#matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg", lw=.7)

matplotlib.pyplot.plot(backleg_targetAngles, label="backleg Target Angles", lw=3)
matplotlib.pyplot.plot(frontleg_targetAngles, label="frontleg Target Angles")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
