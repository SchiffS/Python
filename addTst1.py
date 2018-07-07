#addTst1(A,B):  test of matrix addition under numpy

import numpy as np

def addTst1(A,B):
    """Test of matrix addition under numpy. A,B are of class ndarray"""
    try:
        C = A + B
    except ValueError:
        if np.shape(A) != np.shape(B):
            print('ValueError raised . . Correctly! Reload script for more')
            return(0)
  
    print('returns\n', C)
    if np.shape(A) != np.shape(B):
        print('\nThis is mathematically erroneous\n')
    else: print('\nThis is mathematically correct\n')
    
    return(0)
    
