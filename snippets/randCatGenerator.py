# The following program takes a dictionary of different values and their 
# associated weight and randomly selects one based off this weight.

from random import *

class randCatGenerator:
	def __init__(self):
		self.cat = None
		self.weight = None

	def genRandCat(self, myDict):
		i = 0
		randNum = random()
		for item in myDict:
			if i == 0:
				self.cat = item
				self.weight = myDict[item]
			else:
				totalWeight = self.weight + myDict[item]
				stickProb = self.weight/totalWeight
				switchProb = myDict[item]/totalWeight
				self.weight = self.weight + myDict[item]
				if randNum > stickProb:
					self.cat = item
			i += 1
		return self.cat

if __name__ == '__main__':
	x = {'a' : 1, 'b' : 5, 'c' : 10, 'd': 3}
	myGenerator = randCatGenerator()
	tallys= {}
	catOccured = set()
	for i in range(100):
		gen = myGenerator.genRandCat(x)
		if gen in catOccured:
			tallys[gen] += 1
		else:
			catOccured.add(gen)
			tallys[gen] = 1
	print(tallys)
