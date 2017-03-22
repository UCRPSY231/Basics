def my_mean(input1,input2,input3):
	summed_inputs = input1 + input2 + input3
	mean = summed_inputs/3
	return mean

def my_looped_mean(inputs):
	summed_inputs = 0
	for val in inputs:
		summed_inputs = summed_inputs + val

	return summed_inputs/len(inputs) 

mean_out_2 = my_looped_mean([1,2,3])
print(mean_out_2)

mean_out_1 = my_mean(1,2,3)
print(mean_out_1)

