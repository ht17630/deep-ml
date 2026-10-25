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




def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
#	A_array = np.array(A)
#	T_array = np.array(T)
#	S_array = np.array(S)
	A_array = to_array(A)
	T_array = to_array(T)
	S_array = to_array(S)


	if inverse_2x2(T_array)==None or inverse_2x2(S_array)==None:
		return -1
	else:
		X = np.dot(inverse_2x2(T_array),A_array)
		Y = np.dot(X,S_array)
	return Y.tolist()