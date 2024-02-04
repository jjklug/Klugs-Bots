import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
	def __init__(self, linkName):
		self.linkName = linkName
		self.values = numpy.zeros(999)

	def Get_Value(self, timestep):
		self.values[timestep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
		#print(self.values)
