import pygame.font
class Scoreboard():
	#显示得分信息的类
	def __init__(self,ai_settings,screen,stats):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		#显示得分信息使用的字体设置
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,48)

		#准备初始得分图像 和 历史最高分图像
		self.prep_score()
		self.prep_high_score()
		self.prep_level()

	def prep_score(self):
		"""将得分转为渲染的图像"""
		rounded_score = int(round(self.stats.score,-1))
		score_str ="{:,}".format(rounded_score)

		# score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)


		#将得分放在右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right-20
		self.score_rect.top = 20

	def prep_high_score(self):
		high_score = int(round(self.stats.high_score,-1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)

		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.screen_rect.top

	def prep_level(self):
		"""将等级转换为渲染的图像"""
		self.level_image  = self.font.render(str(self.stats.level),True,self.text_color,self.ai_settings.bg_color)
		#将等级放在得分下方
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top =self.score_rect.bottom + 10

	def show_score(self):
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)





