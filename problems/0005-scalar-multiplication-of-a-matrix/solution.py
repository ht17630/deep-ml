import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	arr = np.array(matrix)
	return (arr*scalar).tolist()


# Using numpy this could have been done without the for loop:
# could have done (arr*scalar).tolist()