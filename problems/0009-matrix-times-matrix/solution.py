import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    ar = np.array(a)
    br = np.array(b)
    if ar.shape[1]!=br.shape[0]:
        return -1
    else:
        c =(np.dot(a,b))
    return c.tolist()