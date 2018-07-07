#addTst2(A,B):  test of matrix addition under numpy with asmatrix()

import numpy as np

def addTst2(A,B):
    """Test of matrix addition under numpy, with A,B typecast as 
'numpy.matrixlib.defmatrix.matrix'"""
    a = np.asmatrix(A)
    b = np.asmatrix(B)
    try:
        C = a + b
    except ValueError:
        if np.shape(a) != np.shape(b):
            print('ValueError raised . . Correctly! Reload script for more')
            return(0)
  
    print('returns\n', C)
    if np.shape(a) != np.shape(b):
        print('\nThis is mathematically erroneous\n')
    else: print('\nThis is mathematically correct\n')
    
    return(0)
    
