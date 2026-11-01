import numpy as np 
def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	matrix_arr = np.array(matrix)
	det = np.linalg.det(matrix_arr)
	tra = np.trace(matrix_arr)
	output_tuple = (det,tra)
	return output_tuple