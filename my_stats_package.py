
class MyStatsPack:
	"""
	This is a sample stats package
	"""
	
	def __init__(self):
		print('Stats Pack Object created')
		some_number = 1

	def my_mean(self,input1,input2,input3):
		summed_inputs = input1 + input2 + input3
		mean = summed_inputs/3
		return mean

	def my_looped_mean(self,inputs):
		summed_inputs = 0
		for val in inputs:
			summed_inputs = summed_inputs + val
		return summed_inputs/len(inputs) 

	def __del__(self):
		print('Stats Pack Object destroyed')

my_stats_pack = MyStatsPack();

mean_out_1 = my_stats_pack.my_mean(1,2,3)
print(mean_out_1)

mean_out_2 = my_stats_pack.my_looped_mean([1,2,3])
print(mean_out_2)

print(some_number)

