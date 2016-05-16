class Arc:

    def __init__(self, metrics, pheromone=1):
        self.metrics = metrics
        self.pheromone = pheromone
    
    def __str__(self):
    	ligne = "M : {}, P : {}\n".format(self.metrics,self.pheromone)
    	return ligne
    