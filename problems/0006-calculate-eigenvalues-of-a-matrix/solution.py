import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

	matrix_array = np.array(matrix)
	eigenvalues = np.linalg.eigvals(matrix_array)
	return eigenvalues.tolist()