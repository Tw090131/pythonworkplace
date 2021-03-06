import pygame
class Ship():
	"""docstring for Ship"""
	def __init__(self,ai_settings,screen):
		#初始化飞船并设置其位置
		self.screen = screen

		#加载飞船图像 并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.ai_settings = ai_settings
		

		#将飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx;
		self.rect.bottom = self.screen_rect.bottom


		#在飞船属性center中存入float类型。 解决rect的centerx只能存int的问题
		self.center = float(self.rect.centerx)
		self.center_y = float(self.rect.centery)

		#设置是否移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		
		#更新飞船的center 值而不是 rect      self.rect.right 飞机矩形的右坐标
		if self.moving_right and self.rect.right <self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		# self.rect.centerx += 1
		
		if self.moving_left and self.rect.left>0:
			self.center -= self.ai_settings.ship_speed_factor

		if self.moving_up and self.rect.top > 0:
			self.center_y -= self.ai_settings.ship_speed_factor
		# self.rect.centerx += 1
		
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.center_y += self.ai_settings.ship_speed_factor

		#根据self.center 的更新rect 对象
		self.rect.centerx = self.center
		self.rect.centery = self.center_y

	def blitme(self):
		"""指定位置 绘制飞船"""
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		self.center = self.screen_rect.centerx
		
		