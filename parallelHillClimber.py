import constants as c
from solution import SOLUTION
import copy

class PARALLEL_HILL_CLIMBER:
	def __init__(self):
		self.nextAvailableID = 0
		self.parents = {}
		for i in range(c.populationSize):
			self.parents[i] = SOLUTION(self.nextAvailableID)
			self.nextAvailableID+=1
		


	def evolve(self):
		for key in self.parents:
			self.parents[key].Evaluate("GUI")
		#self.parent.Evaluate("GUI")
		#for currentGeneration in range(c.numberOfGenerations):
			#self.Evolve_For_One_Generation()
		pass
	
	def Evolve_For_One_Generation(self):
		self.Spawn()

		self.Mutate()

		self.child.Evaluate("DIRECT")

		self.Print()

		self.Select()

	def Spawn(self):
		self.child = copy.deepcopy(self.parent)
		self.child.Set_ID(nextAvailableID)
		self.nextAvailableID+=1

	def Mutate(self):
		self.child.Mutate()
		#print(self.parent.weights)
		#print(self.child.weights)
		
	
	def Select(self):
		if(self.parent.fitness > self.child.fitness):
			self.parent = self.child

	def Print(self):
		print("\nParent:" + str(self.parent.fitness) + ", " + "Child: " + str(self.child.fitness))

	def Show_Best(self):
		#self.parent.Evaluate("GUI")
		pass