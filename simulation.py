from world import WORLD
from robot import ROBOT
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time


class SIMULATION:
	def __init__(self, directOrGui):
		#initial setup stuff
		if directOrGui == "DIRECT":
				self.physicsClient = p.connect(p.DIRECT)
		if directOrGui == "GUI":
			self.physicsClient = p.connect(p.GUI)
		p.setGravity(0,0,-9.8)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		

		self.world = WORLD()
		self.robot = ROBOT()


	def Run(self):
		#for loop that runs the simulation
		for i in range(999):
			#time.sleep(1/60)
			p.stepSimulation()
			self.robot.Sense(i)
			self.robot.Think()
			self.robot.Act(i)

	def __del__(self):
		p.disconnect()

	def Get_Fitness(self):
		self.robot.Get_Fitness()