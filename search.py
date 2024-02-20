import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

os.system("del brain*.nndf")
os.system("del fitness*.txt")

phc = PARALLEL_HILL_CLIMBER()
phc.evolve()
#phc.Show_Best()