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
		self.Evaluate(self.parents)
		for currentGeneration in range(c.numberOfGenerations):
			self.Evolve_For_One_Generation()
	
	def Evolve_For_One_Generation(self):
		self.Spawn()

		self.Mutate()

		self.Evaluate(self.children)

		self.Print()

		self.Select()

	def Spawn(self):
		self.children = {}
		for key in self.parents:
			self.children[key] = copy.deepcopy(self.parents[key])
			self.children[key].Set_ID(self.nextAvailableID)
			self.nextAvailableID+=1

	def Mutate(self):
		for key in self.children:
			self.children[key].Mutate()
	
	def Evaluate(self, solutions):
		for key in solutions:
			solutions[key].Start_Simulation("DIRECT")
		for key in solutions:
			solutions[key].Wait_For_Simulation_To_End()
	
	def Select(self):
		for key in self.parents:
			if(self.parents[key].fitness > self.children[key].fitness):
				self.parents[key] = self.children[key]

	def Print(self):
		for key in self.parents:
			print("\nParent:" + str(self.parents[key].fitness) + ", " + "Child: " + str(self.children[key].fitness))

	def Show_Best(self):
		best = 0
		for key in self.parents:
			if self.parents[key].fitness < self.parents[best].fitness:
				best = key
		self.parents[best].Start_Simulation("GUI")
