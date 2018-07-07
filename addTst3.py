#addTst3(A,B):  test of matrix addition under scipy

import scipy as sp

def addTst3(A,B):
    """Test of matrix addition under scipy. A,B are of class ndarray"""
    try:
        C = A + B
    except ValueError:
        if sp.shape(A) != sp.shape(B):
            print('ValueError raised . . Correctly! Reload script for more')
            return(0)
  
    print('returns\n', C)
    if sp.shape(A) != sp.shape(B):
        print('\nThis is mathematically erroneous\n')
    else: print('\nThis is mathematically correct\n')
    
    return(0)
    
