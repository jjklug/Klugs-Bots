import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import constants as c
import time

class SOLUTION:
	length = 1
	width = 1
	x = 0
	y = 0
	z = 0.5


	def __init__(self, nextAvailableID):
		self.myID = nextAvailableID
		self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
		self.weights = (self.weights*2)-1

	def Start_Simulation(self, directOrGUI):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		os.system("start /B py simulate.py " + directOrGUI + " " + str(self.myID))

	def Wait_For_Simulation_To_End(self):
		while not os.path.exists("fitness" + str(self.myID) + ".txt"):
			time.sleep(0.01)
		fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
		self.fitness = float(fitnessFile.read())
		fitnessFile.close()
		os.system("del fitness" + str(self.myID) + ".txt")

	def Create_World(self):
		pyrosim.Start_SDF("world.sdf")
		pyrosim.Send_Cube(name="Box" , pos=[self.x-3,self.y+2,self.z] , size=[1,1,1])
		pyrosim.End()

	def Create_Body(self):
		pyrosim.Start_URDF("body.urdf")
		pyrosim.Send_Cube(name="Torso" , pos=[1.5, 0, 1.5] , size=[1,1,1])
		pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
		pyrosim.Send_Cube(name="BackLeg" , pos=[-0.5,0,-0.5] , size=[1,1,1])
		pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
		pyrosim.Send_Cube(name="FrontLeg" , pos=[0.5,0,-0.5] , size=[1,1,1])
		pyrosim.End()

	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
		pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
		pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

		for currentRow in range(c.numSensorNeurons):
			for currentColumn in range(c.numMotorNeurons):
				pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn+c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])	
		pyrosim.End()

	def Mutate(self):
		randomRow = random.randint(0,c.numSensorNeurons-1)
		randomColumn = random.randint(0,c.numMotorNeurons-1)
		self.weights[randomRow][randomColumn] = random.random()*2-1

	def Set_ID(self, nextAvailableID):
		self.myID = nextAvailableID