from arc import *
from environment import *

listNodes = ["A", "B", "C", "D", "E", "F", "N"]
#           A         B       C       D      E        F        N
matrix = [[Arc(0), Arc(0), Arc(5), Arc(0), Arc(0), Arc(0), Arc(5)],  # A
          [Arc(0), Arc(0), Arc(1), Arc(0), Arc(0), Arc(0), Arc(1)],  # B
          [Arc(5), Arc(1), Arc(0), Arc(4), Arc(1), Arc(0), Arc(0)],  # C
          [Arc(0), Arc(0), Arc(4), Arc(0), Arc(0), Arc(3), Arc(0)],  # D
          [Arc(0), Arc(0), Arc(1), Arc(0), Arc(0), Arc(1), Arc(0)],  # E
          [Arc(0), Arc(0), Arc(0), Arc(3), Arc(1), Arc(0), Arc(0)],  # F
          [Arc(5), Arc(1), Arc(0), Arc(0), Arc(0), Arc(0), Arc(0)]]  # N
mainEnvironment = Environment(listNodes, matrix)
