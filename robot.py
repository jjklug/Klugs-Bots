from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim

class ROBOT:
	def __init__(self):
		self.robotId = p.loadURDF("body.urdf")
		self.motors = {}

		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()

	def Prepare_To_Sense(self):
		self.sensors = {}
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)
	
	def Sense(self, timestep):
		for x in self.sensors:
			self.sensors[x].Get_Value(timestep)