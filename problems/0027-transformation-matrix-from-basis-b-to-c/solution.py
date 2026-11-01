import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    matrix_array = np.array(matrix)
    if np.linalg.det(matrix_array)==0:
        return None
    else:
        matrix_inverse = np.linalg.inv(matrix_array)
    return matrix_inverse.tolist()

def to_array(matrix: list[list[float]]):
	return np.array(matrix)


def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	B_ar = to_array(B)
	C_arr = to_array(C)
	P_arr = np.dot(inverse_2x2(C),B)


	return P_arr.tolist()