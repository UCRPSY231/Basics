
class MyArray: 
	"""
	This is a sample stats package
	"""
	
	def __init__(self,init_values): #Every class should have an init function, this runs when an instance is created
		self.array_values = init_values

	def my_looped_mean(self):
		summed_inputs = 0
		for val in self.array_values:
			summed_inputs = summed_inputs + val
		return summed_inputs/len(self.array_values) 

my_array = MyArray([1,2,3]); #We created an instance of the MyArray class 

mean_out = my_array.my_looped_mean()
print(mean_out)

