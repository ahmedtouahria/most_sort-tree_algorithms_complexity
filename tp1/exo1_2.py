import random  # for handel random number
import time
import numpy as np
"""====== question 2 ======"""

from functions.utils import array_of_random



"""======= question 1 part2 ========="""


def classic_matrix_mult(X, Y, n):
    # X = matrix X
    # Y = matrix Y
    #  n = matrix type N*N
    # result is n*n
    result = [] # for generate [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] and assign final result
    inner_result = [] # for generate matrix [0, 0, 0, 0] 
    start = time.time() # start time for complixity time count
    """this part generate n*n matrix of 0 """
    for i in range(n):
        for j in range(1):
            inner_result.append(0)# for generate [0, 0, 0, 0]
        result.append(inner_result)
    """"""
    # iterate through rows of X
    # print("result:",result)
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j] # matrix multiply logic 
    end = time.time() # final time for complixity time
    #print("The time of execution of above script is :",(end-start) * 10**3, "ms")
    #print("result of A*B = ", result)
# test function 
classic_matrix_mult(X = [[12,7,3,4],[4 ,5,6,4],[7 ,8,9,4],[17 ,2,3,4]],Y = [[5,8,1,4],[6,7,3,4],[4,5,9,4],[7,3,9,4]],n=4)


""" ================ question 2 Part 2 ==================="""


""" ================ question 3 Part 2 ==================="""


def gen_matrix(n, start_random, end_random):
    # result is n*n
    result = []
    inner_result = []
    for i in range(n):
        result.append(array_of_random(n)) # append random table
    print(result)
gen_matrix(5,1,9)

""" ========== Question 5 ========== """



# Version 3.6


def split(matrix):
	"""
	Splits a given matrix into quarters.
	Input: nxn matrix
	Output: tuple containing 4 n/2 x n/2 matrices corresponding to a, b, c, d
	"""
	row, col = matrix.shape
	row2, col2 = row//2, col//2
	return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen(x, y):
	"""
	Computes matrix product by divide and conquer approach, recursively.
	Input: nxn matrices x and y
	Output: nxn matrix, product of x and y
	"""

	# Base case when size of matrices is 1x1
	if len(x) == 1:
		return x * y

	# Splitting the matrices into quadrants. This will be done recursively
	# until the base case is reached.
	a, b, c, d = split(x)
	e, f, g, h = split(y)

	# Computing the 7 products, recursively (p1, p2...p7)
	p1 = strassen(a, f - h)
	p2 = strassen(a + b, h)		
	p3 = strassen(c + d, e)		
	p4 = strassen(d, g - e)		
	p5 = strassen(a + d, e + h)		
	p6 = strassen(b - d, g + h)
	p7 = strassen(a - c, e + f)

	# Computing the values of the 4 quadrants of the final matrix c
	c11 = p5 + p4 - p2 + p6
	c12 = p1 + p2		
	c21 = p3 + p4			
	c22 = p1 + p5 - p3 - p7

	# Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
	c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

	return c
def time_between_numpy_and_other(X,Y,n):
    start = time.time() 
    np.dot(X,Y)
    end = time.time() 
    print("The time of execution of above numpy script is :",(end-start) * 10**3, "ms")
    start = time.time() 
    classic_matrix_mult(X,Y,n)
    end  = time.time() 
    print("The time of execution of above classic_matrix_mult script is :",(end-start) * 10**3, "ms")
    start = time.time() 
    strassen(X,Y)
    end = time.time() 
    print("The time of execution of above strassen algorithm is :",(end-start) * 10**3, "ms")

time_between_numpy_and_other(X = np.array([[12,7,3,4],[4 ,5,6,4],[7 ,8,9,4],[17 ,2,3,4]]),Y = np.array([[5,8,1,4],[6,7,3,4],[4,5,9,4],[7,3,9,4]]),n=4)