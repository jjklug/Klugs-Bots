import constants as c
from solution import SOLUTION
import copy

class HILL_CLIMBER:
	def __init__(self):
		self.parent = SOLUTION()

	def evolve(self):
		self.parent.Evaluate("GUI")
		for currentGeneration in range(c.numberOfGenerations):
			self.Evolve_For_One_Generation()
	
	def Evolve_For_One_Generation(self):
		self.Spawn()

		self.Mutate()

		self.child.Evaluate("DIRECT")

		self.Print()

		self.Select()

	def Spawn(self):
		self.child = copy.deepcopy(self.parent)

	def Mutate(self):
		self.child.Mutate()
		#print(self.parent.weights)
		#print(self.child.weights)
		
	
	def Select(self):
		if(self.parent.fitness > self.child.fitness):
			self.parent = self.child

	def Print(self):
		print("\nParent:" + str(self.parent.fitness) + ", " + "Child: " + str(self.child.fitness))

	def Show_Best():
		self.parent.Evaluate("GUI")