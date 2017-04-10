import numpy as np
#Inputs are seperated by commas
#Functions must be defined before being called
def my_mean(input1,input2,input3): 
	"""Calculates the mean of 3 numbers"""
	summed_inputs = input1 + input2 + input3
	mean = summed_inputs/3
	return mean

def my_looped_mean(inputs):
	"""Calculates the mean of a list of numbers"""
	summed_inputs = 0
	for val in inputs:
		if np.isnan(val):
			raise Exception('NaN in list is not supported')
		summed_inputs = summed_inputs + val

	return summed_inputs/len(inputs) 


print('We start here')

mean_out_1 = my_mean(1,2,3)
print(mean_out_1)

mean_out_2 = my_mean(1,input3=2,input2=3)
print(mean_out_2)


mean_out_3 = my_looped_mean([1,2,3])
print(mean_out_3)

mean_out_4 = my_looped_mean([1,2,np.nan])
print(mean_out_4)

