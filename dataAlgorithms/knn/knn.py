import numpy as np

class nearest_neighbors:
	
	def __init__(self, target, train, labels):
		self.target_array = target
		self.train_data = train
		self.labels = labels
		self.distances = ((np.tile(target, (train.shape[0],1)) - train)**2).sum(axis = 1)**0.5
		self.distances_order = self.distances.argsort()

	def k_nearest(self, k):
		votes = {}
		for i in range(k):
			votelabel = self.labels[i]
			votes[votelabel] = votes.get(votelabel,0) + 1
		sortedVotes = sorted(votes.iteritems())
		return sortedVotes[0][0]
