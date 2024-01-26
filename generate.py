import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

for j in range(5):
	x=0
	for k in range(5):
		length = 1
		width = 1
		height = 1
		z=.5
		for i in range(9):
			length*=.9
			width*=.9
			height*=.9
			z+=1
			pyrosim.Send_Cube(name="Box" , pos=[x,y,z] , size=[length,width,height])
		x+=1
	y+=1


pyrosim.End()