class Restaurant():
	def __init__(self,restaurnat_name,cuisine_type):
		self.restaurnat_name = restaurnat_name
		#cuisine 美食
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("restaurant describetion")

	def open_restaurant(self):
		print("open restaurant")

	def show_served(self):
		print(self.number_served)

	def set_number_served(self,num):
		self.number_served = num
		print("set_number_served is : "+ str(num))

	def incremen_number_served(self,addnum=1):
		self.number_served += addnum
		print("now number_served is : "+str(self.number_served))


restaurant = Restaurant('zzw','pizza')
restaurant.show_served()
restaurant.set_number_served(100)
restaurant.incremen_number_served()
restaurant.incremen_number_served()



