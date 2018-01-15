import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

##page 277页开始没写代码
def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	#设置标题
	pygame.display.set_caption("Alien invasion")

	#创建play按钮
	play_button = Button(ai_settings,screen,"play")
	
	#创建一个用于统计游戏信息的实例
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)

	#设置背景色
	bg_color = ai_settings.bg_color
	screen.fill(bg_color)

	#创建一艘飞船
	ship = Ship(ai_settings,screen)


	#创建一个用于存储子弹的编组
	bullets = Group()

	#创建一个外星人
	aliens = Group()
	gf.create_fleet(ai_settings,screen,ship,aliens)

	#开始游戏的主循环
	while True:
		#监听键盘和鼠标事件
		gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)

		if stats.game_active :
			#更新飞船位置
			ship.update()
			#子弹的更新和删除
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)


		#绘制屏幕
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
		# ship.blitme()
		# #让最近绘制的屏幕可见(更新屏幕绘制)
		# pygame.display.flip()
		


run_game()