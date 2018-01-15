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

lili = User("lili","swift",age="18",sex="female")
lili.describe_user()
lili.greet_user()
