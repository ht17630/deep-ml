import numpy as np

def make_diagonal(x):
	#eye = np.eye(len(x))
	return np.multiply(x,np.eye(len(x)))