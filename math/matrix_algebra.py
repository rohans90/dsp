# Matrix Algebra



import numpy as np

A = np.matrix([[1,2,3],[2,7,4]])

B = np.matrix([[1,-1],[0,1]])

C = np.matrix([[5,-1],[9,1],[6,0]])

D = np.matrix([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])

w = np.array([1,8,0,5])
w.shape = (4,1)

u+v
##array([ 9,  7, -4,  9])

u-v
##array([ 3, -3, -2,  1])

6*u
##array([ 36,  12, -18,  30])

u*v
##array([18, 10,  3, 20])

||u||
s = ((np.sum(i**2 for i in u)))
print (s**0.5)
##8.60232526704


##Q3

A+C
##Not Defined

D = C.transpose()
A-D
##Out[172]: 
#matrix([[-4, -7, -3],
 #       [ 3,  6,  4]])

C.transpose()+3*D
##matrix([[20, 36, 24],
#        [-4,  4,  0]])

B*A
#matrix([[-1, -5, -1],
 #       [ 2,  7,  4]])

B*(A.transpose())
##Not defined

B*C
##Not defined

C*B
#matrix([[ 5, -6],
#        [ 9, -8],
#        [ 6, -6]])

B**4
#matrix([[ 1, -4],
  #      [ 0,  1]])

A*(A.transpose())
#matrix([[14, 28],
 #       [28, 69]])

(D.transpose())*D
#matrix([[26, 44, 30],
#        [44, 82, 54],
#        [30, 54, 36]])
