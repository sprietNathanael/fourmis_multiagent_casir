from arc import *
from environment import *
from ant import *

def startSimulation(environment):
	ants = environment.ants
	graph = environment.graph
	for ant in  ants:
		ant.act(environment)


if __name__ == '__main__':
	# Initilisation des classe
	listNodes = {"A":0, 
				 "B":1, 
				 "C":2, 
				 "D":3, 
				 "E":4, 
				 "F":5, 
				 "N":6}
	#           A         B       C       D      E        F        N
	matrix = [[Arc(0), Arc(0), Arc(5), Arc(0), Arc(0), Arc(0), Arc(5)],  # A
			  [Arc(0), Arc(0), Arc(1), Arc(0), Arc(0), Arc(0), Arc(1)],  # B
			  [Arc(5), Arc(1), Arc(0), Arc(4), Arc(1), Arc(0), Arc(0)],  # C
			  [Arc(0), Arc(0), Arc(4), Arc(0), Arc(0), Arc(3), Arc(0)],  # D
			  [Arc(0), Arc(0), Arc(1), Arc(0), Arc(0), Arc(1), Arc(0)],  # E
			  [Arc(0), Arc(0), Arc(0), Arc(3), Arc(1), Arc(0), Arc(0)],  # F
			  [Arc(5), Arc(1), Arc(0), Arc(0), Arc(0), Arc(0), Arc(0)]]  # N

	ants = [Ant()]
	mainEnvironment = Environment(listNodes, matrix, ants)
	startSimulation(mainEnvironment)