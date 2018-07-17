# PythonTopic:  Matrix addition and subtraction errors in Python
Software:  Python 3.6.2 (64 bit) with Scipy and Numpy; Python 2.7.10 (32 bit) with Scipy and Numpy
Date:  6 July 2018

According to any text on matrix math or linear algebra, the sum or difference of two matrices exists only if the two matrices are of the same order, which is to say, they have the same number of rows and columns.  Addition or subtraction is defined element-wise; if Aij is the element of A in the ith row and jth column, adding or subtracting B from A is accomplished by forming Cij = Aij +(or)- Bij, over the entire matrices A, B.

In Python, the order of an array is given by numpy.shape(), which returns a tuple with two elements, in the case of a 2-dimensional array.  Thus the condition for the existence of the sum or difference between the matrices A and B (of type ndarray) is that numpy.shape(A) == numpy.shape(B) returns True.  As I found out after wasting time creating this repository and filing a bug report, the behavior observed is by design (broadcasting) and has uses in applications other than linear algebra.  Thus the only useful purpose this repository might serve is to warn others who might happen upon it that numpy and scipy allow column or row vectors to be added to matrices of arbitrary shapes, so long as the number of rows or columns, respectively, match those of the column or row vector.  GIGO, in other words.

I have found that if A is an n x m matrix and B is a row or column vector that otherwise matches A, then under both versions of Python, using either the Numpy or Scipy library, and in the former case even when the arrays are further typecast using numpy.asmatrix(), the sum or difference A +or- B returns a matrix in which the elements of B are added or subtracted, as the case may be, from all the rows or columns of A.  This is not correct.  The correct behavior would be for Python to throw a ValueError, specifying the mismatch in array shapes.  Indeed, this is the behavior if B is anything but a column or row matrix.

In other words, if for example A is 3 x 3 and B is 1 x 3 or 3 x 1, then Python erroneously allows addition or subtraction of the two.  But if C is a 3 x 2, for instance, an attempt to add or subtract them returns the error message

	Traceback (most recent call last):
  	  File "<pyshell#3>", line 1, in <module>
    	    A+B
	ValueError: operands could not be broadcast together with shapes (3,3) (3,2)

which is correct.
