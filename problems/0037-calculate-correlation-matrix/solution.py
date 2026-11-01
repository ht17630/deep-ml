import numpy as np

def calculate_correlation_matrix(X, Y=None):
    X = np.array(X)

    if Y is None:
        return np.corrcoef(X,rowvar=False)

    Y = np.array(Y)

    result = np.zeros((len(X), len(Y)))

    for i in range(len(X)):
        for j in range(len(Y)):
            result[i, j] = np.corrcoef(X[i], Y[j])[0, 1]

    return result