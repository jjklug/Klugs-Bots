import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
	def __init__(self, jointName):
		self.jointName = jointName
		self.Prepare_To_Act()

	def Prepare_To_Act(self):
		self.amplitude = c.amplitude

		#conditional to half frequency of one leg
		jname = self.jointName.decode()
		if jname == "Torso_BackLeg":
			self.frequency = c.frequency/2
		else:
			self.frequency = c.frequency

		self.offset = c.phaseOffset

		targetAngles = numpy.linspace(0, 2*int(numpy.pi), 999)
		self.motorValues = (self.amplitude)*numpy.sin(self.frequency*targetAngles+self.offset)

	def Set_Value(self, robot, timestep):
		pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[timestep], maxForce=25)

	#saving data to files
	def Save_Values(self):
		numpy.save("data/motorValues.npy", motorValues)