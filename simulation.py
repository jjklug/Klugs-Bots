from world import WORLD
from robot import ROBOT
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time


class SIMULATION:
	def __init__(self):
		#initial setup stuff
		self.physicsClient = p.connect(p.GUI)
		p.setGravity(0,0,-9.8)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		

		self.world = WORLD()
		self.robot = ROBOT()

		pyrosim.Prepare_To_Simulate(self.robot.robotId)

	def Run(self):
		#for loop that runs the simulation
		for i in range(999):
			print(i)
			time.sleep(1/60)
			p.stepSimulation()
			#backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
			#frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
		
			#pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = backleg_targetAngles[i], maxForce=25)
			#pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = frontleg_targetAngles[i], maxForce= 25)

	def __del__(self):
		p.disconnect()