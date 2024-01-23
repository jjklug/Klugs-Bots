import pybullet as p
physicsClient = p.connect(p.GUI)

for i in range(999):
	p.stepSimulation()


p.disconnect()