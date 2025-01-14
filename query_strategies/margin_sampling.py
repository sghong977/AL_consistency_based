import numpy as np
from .strategy import Strategy

class MarginSampling(Strategy):
	def __init__(self, X, Y, idxs_lb, net, handler, args,  al_apply=False, cm_train_apply=False):
		super(MarginSampling, self).__init__(X, Y, idxs_lb, net, handler, args,  al_apply=al_apply, cm_train_apply=cm_train_apply)

	def query(self, n):
		idxs_unlabeled = np.arange(self.n_pool)[~self.idxs_lb]
		probs = self.predict_prob(self.X[idxs_unlabeled], self.Y[idxs_unlabeled])
		probs_sorted, idxs = probs.sort(descending=True)
		U = probs_sorted[:, 0] - probs_sorted[:,1]
		return idxs_unlabeled[U.sort()[1][:n]]
