class Settings():
	"""存储游戏的所有设置"""
	def __init__(self):
		"""初始化游戏的设置"""
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		#飞船的速度
		self.ship_speed_factor = 5.5
		#玩家剩余飞船数	
		self.ship_limit = 3

		#子弹设置
		self.bullet_speed_factor = 3
		self.bullet_width = 1000
		self.bullet_height =15
		self.bullet_color = 60,60,60	
		self.bullets_allowed = 500


		#外星人属性
		self.alien_speed_factor = 10
		#撞到边缘 向下的速度
		self.fleet_drop_speed = 30
		#fleet_direction 为1向右 -1向左
		self.fleet_direction = 1


		#以什么样的速度加快游戏
		self.speedup_scale = 1.1
		#外星人点数的提高速度
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

		self.alien_point = 50

	def initialize_dynamic_settings(self):
		#初始化随着游戏进行而改变的设置
		self.ship_speed_factor = 5.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 10

		self.fleet_direction = 1


	def increase_speed(self):
		#提高速度设置
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_point = int(self.alien_point * self.score_scale)

		