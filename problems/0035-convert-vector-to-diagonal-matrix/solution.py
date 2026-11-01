import numpy as np

def make_diagonal(x):
	eye = np.eye(len(x))
	output = np.multiply(x,eye)
	return output