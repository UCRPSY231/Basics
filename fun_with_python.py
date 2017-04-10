import numpy as np

matrix_1 = np.matrix([[1,1,1],
					  [2,2,2],
					  [3,3,3]])

print(np.mean(matrix_1,axis=0)) #Function call

print(matrix_1.mean(axis=0)) #Method call


#Chaining function calls
print(matrix_1.max().mean())

print(matrix_1.mean().max())

#Better
print((matrix_1.max()).mean())