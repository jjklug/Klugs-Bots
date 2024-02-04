import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy
import random

#initial setup stuff

#motor variables
backleg_amplitude = numpy.pi/4
backleg_frequency = 10.5
backleg_phaseOffset = 0

frontleg_amplitude = numpy.pi/4
frontleg_frequency = 10.5
frontleg_phaseOffset = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

#sensor and motor value arrays created below
backLegSensorValues = numpy.zeros(999)
frontLegSensorValues = numpy.zeros(999)
targetAngles = numpy.linspace(0, 2*int(numpy.pi), 999)
backleg_targetAngles = (backleg_amplitude)*numpy.sin(backleg_frequency*targetAngles+backleg_phaseOffset)
frontleg_targetAngles = (frontleg_amplitude)*numpy.sin(frontleg_frequency*targetAngles+frontleg_phaseOffset)
numpy.save("data/targetAngles.npy", targetAngles)



#for loop that runs the simulation
for i in range(999):
	time.sleep(1/60)
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = backleg_targetAngles[i], maxForce=25)
	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = frontleg_targetAngles[i], maxForce= 25)




p.disconnect()

#saving data to files
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
