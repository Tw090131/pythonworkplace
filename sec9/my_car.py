
""" 一个模块中放多个类。可以 分别引用"""
# from car import Car

# my_car = Car('audi','a5',2017)
# print(my_car.get_descriptive_name())

import car 
# me = User('ZHANG','ZHIWEI')
# me.describe_user()

class Las():
	def __init__(self):
		
		self.aaa = car.User("li",'wei')

ls = Las()
ls.aaa.describe_user()