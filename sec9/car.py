class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year)+' '+ self.make + ' ' +self.model
		return long_name.title()

	def read_odometer(self):
		print("odometer is:"+str(self.odometer_reading))



class User():
	"""docstring for User"""
	def __init__(self, first_name,last_name,**opt):
		self.first_name = first_name
		self.last_name = last_name
		self.opt = {}
		for key,val in opt.items():
			self.opt[key] = val

	def describe_user(self):
		print("my name is" + self.first_name +"."+self.last_name)
		print(self.opt)

	def greet_user(self):
		print("hello,"+self.first_name+'.'+self.last_name)

