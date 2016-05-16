import random
class Ant:

	def __init__(self, status="F", position="A"):
		# F : Forward
		# B : Backward
		# D : Dead
		self.status = status
		self.position = position
		self.road = [position]

	def __str__(self):
		line1 = "status : {}\n".format(self.status)
		line2 = "position : {}\n".format(self.position)
		line3 = "road : {}\n".format(self.road)
		return (line1+line2+line3)

	def act(self,environment):
		# Si position = debut
		# suicide
		
		# Switch
		# case status = F
		# recuperer suivant possible
		# tirer un hasard
		# prendre le cheminsuivant
		# case status = B
		# recuperer position precedent dans road
		# placer sur position precedente

		print ('loul')

	def suicide(self):
		random.randint(1, 10)
		print("JE MEURS DANS D'ATTROCE SOUFRANCE")
		self.status = 'D'