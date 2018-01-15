class Privileges():
	def __init__(self,privileges):
		self.privileges = privileges

	def show_privileges(self):
		print("privileges is::")
		for i in self.privileges:
			print(i)

	