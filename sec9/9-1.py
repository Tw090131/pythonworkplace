class Restaurant():
	def __init__(self,restaurnat_name,cuisine_type):
		self.restaurnat_name = restaurnat_name
		#cuisine 美食
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("restaurant describetion")

	def open_restaurant(self):
		print("open restaurant")



restaurant = Restaurant('zzw','pizza')
restaurant.describe_restaurant()
restaurant.open_restaurant()



