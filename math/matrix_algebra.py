# h-rm_tan 28Aug2016

#==============================================================================
# # Refs
#==============================================================================
# http://stackoverflow.com/questions/3127404/how-to-represent-matrices-in-python
# https://www.ibm.com/developerworks/community/blogs/jfp/entry/Elementary_Matrix_Operations_In_Python?lang=en
# http://www.python-course.eu/matrix_arithmetic.php


#==============================================================================
# # Matrix Algebra
#==============================================================================

#PLACE YOUR CODE HERE

#from numpy import matrix
#from numpy import array
#from numpy import linalg

import numpy as np


A = np.matrix ([[1, 2, 3] , [2, 7, 4]] )

B = np.matrix ([[1, -1] , [0, 1]] )

C = np.matrix ([[5, -1] , [9, 1] , [6, 0]] )

D = np.matrix ([[3, -2, -1] , [1, 2, 3]] )

u = np.array([6, 2, -3, 5])[None,:]

v = np.array([3, 5, -1, 4])[None,:]

w = np.array([1, 8, 0, 5])[:, None]


#==============================================================================
# #1. Matrix Dimensions
#==============================================================================

np.shape(A)
#>>> (2, 3)
np.shape(B)
#>>> (2, 2)
np.shape(C)
#(3, 2)
np.shape(D)
#(2, 3)
np.shape(u)
#(1, 4)  # without u[None,:] shape info=(4,)  # 1x4
np.shape(v)
#(1, 4)  # 1x4
np.shape(w)
#(4, 1)


#==============================================================================
# #2. Vector Operations
# #Perform the following operations. Assume
alpha = 6.
#==============================================================================
alpha = 6

#2.1) u + v =
u + v
#array([[ 9,  7, -4,  9]])

#2.2) u - v =
u - v
#array([[ 3, -3, -2,  1]])

#2.3)
alpha*u =
alpha*u
#array([[ 36,  12, -18,  30]])

#2.4) u.v = u1v1 + u2v2 + u3v3 == np.sum(u*v)
## np.dot(a,b) works for vectors only if they are 1dim
np.dot(u.reshape(u.size,),v.reshape(v.size,))
#51

#2.5) ||u|| = sqrt(u1^2 + u2^2 + u3^2)
np.linalg.norm(u)
#8.6023252670426267



#==============================================================================
# #3. Matrix Operations
# #Evaluate each of the following expressions, if it is defined; else fill in with "not defined."
#==============================================================================

#3.1) A + C = NOT DEFINED
#ValueError: operands could not be broadcast together with shapes (2,3) (3,2)

#3.2) A - C^T =
#A - C.transpose()
A - C.T
#matrix([[-4, -7, -3],
#        [ 3,  6,  4]])

#3.3) C^T + 3*D =
#C.transpose() + 3*D
C.T + 3*D
#matrix([[14,  3,  3],
#        [ 2,  7,  9]])

#3.4) BA =
B*A
#matrix([[-1, -5, -1],
#        [ 2,  7,  4]])

#3.5) BA^T = NOT DEFINED
#B*A.transpose()
B*A.T
#ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)


#==============================================================================
# #Optional
#==============================================================================

#3.6) BC =
B*C
#ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)

#3.7) CB =
C*B
#matrix([[ 5, -6],
#        [ 9, -8],
#        [ 6, -6]])

#3.8) B^4 =
B*B*B*B
#matrix([[ 1, -4],
#        [ 0,  1]])

#3.9) AA^T =
#A*A.transpose()
A*A.T
#matrix([[14, 28],
#        [28, 69]])

#3.10) D^TD =
#D.transpose()*D
D.T*D
#matrix([[10, -4,  0],
#        [-4,  8,  8],
#        [ 0,  8, 10]])

