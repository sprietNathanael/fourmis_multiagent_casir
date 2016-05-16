class Environment:

	def __init__(self, listNodes, graph,ants):
		self.graph = graph
		self.listNodes = listNodes
		self.ants = ants
	def getArc(self,x,y):
		return self.graph[self.listNodes[x]][self.listNodes[y]]

	def getLetterByNumber(x,y):
		# pas fini
		return'l','m'