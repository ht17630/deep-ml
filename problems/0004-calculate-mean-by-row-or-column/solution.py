import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means =[]
	if mode == 'column':
		for j in range(len(matrix[0])):
			matrix_column = np.array(matrix)[:,j]
			means.append(np.mean(matrix_column))
	else:
		for j in range(len(matrix)):
				matrix_row = np.array(matrix)[j,:]
				means.append(np.mean(matrix_row))
		
	
	# This code could have been done more efficinetly if I understand numpy better
	# To do column it is arr = np.array(matrix) 
	# return np.mean(arr,axis=0).tolist()
	# So numpy has a built in function for what I was trying to do. 
	
	
	
	
	return means