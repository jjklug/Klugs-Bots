from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK



class ROBOT:
	def __init__(self):
		self.robot = p.loadURDF("body.urdf")
		self.nn = NEURAL_NETWORK("brain.nndf")

		pyrosim.Prepare_To_Simulate(self.robot)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()

	def Prepare_To_Sense(self):
		self.sensors = {}
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)
	
	def Sense(self, timestep):
		for x in self.sensors:
			self.sensors[x].Get_Value(timestep)

	def Prepare_To_Act(self):
		self.motors = {}
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)

	def Act(self, timestep):
		for x in self.motors:
			self.motors[x].Set_Value(self.robot, timestep)

	def Think(self):
		self.nn.Update()
		self.nn.Print()


