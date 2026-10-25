import numpy as np
def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	a_1 = np.array(a)
	b_1 = np.array(b)
	if len(a)!=len(b):
		return -1
	else:
		added_vectors = np.add(a_1,b_1)


	return added_vectors.tolist()