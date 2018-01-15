import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
	if stats.ships_left > 0:
		stats.ships_left -= 1
		#清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()

		#创建一群新的外星人，并将飞船充值底部中央
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()

		#暂停	
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
	"""检测是否有外星人到达屏幕底部"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
			break

def check_fleet_edges(ai_settings,aliens):
	"""外星人到达边缘措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			# 只要有一个到达底部9⃣️break
			break

def change_fleet_direction(ai_settings,aliens):
	"""将整群外星人下移，并改变它们的方向"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
	check_fleet_edges(ai_settings,aliens)
	"""更细aliens的位置"""
	aliens.update()
	#检测外星人和飞船之间的碰撞 spritecollideany 接受一个精灵和一个编组
	#发送碰撞 将停止遍历编组，返回第一个与飞船碰撞的外星人
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats,screen,ship,aliens,bullets)

	#检查是否有外星人到达底部
	check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)

def create_fleet(ai_settings,screen,ship,aliens):
	"""创建外星人群"""
	#创建一个外星人，并计算一行可容纳多少外星人
	#外星人之间的间距为外星人的宽度
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,row_number)
		
def get_number_rows(ai_settings,ship_height,alien_height):
	"""计算屏幕可以容纳多少外星人"""
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows		

def get_number_aliens_x(ai_settings,alien_width):
	#计算每行能容纳多少外星人
	available_space_x = ai_settings.screen_width - 2*alien_width
	number_aliens_x = int(available_space_x / (2*alien_width))
	return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	"""创建一个外星人并将其放在当前行"""
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
	"""更新子弹的位置 ，并删除已经消失的子弹"""
	"""更新子弹位置"""
	bullets.update()
	#删除已删除的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)
	
def check_high_score(stats,sb):
	"""检查是否诞生了最高分"""

	if stats.score > stats.high_score:

		stats.high_score = stats.score
		sb.prep_high_score()

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
	#检查是否有子弹击中了外星人，如果有就删除相应的子弹和外星人。
	#{bullets1 : alien1} , groupcollide 检测有碰撞9⃣️在返回的字典中添加一个键值对，两个true表明删除发生碰撞的子弹和外星人
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

	#加分
	if collisions:
		for alien in collisions.values():
			stats.score += ai_settings.alien_point * len(alien)
			sb.prep_score()
		check_high_score(stats,sb)

	if len(aliens) == 0 :
		#删除现有的子弹并新建一批外星人
		bullets.empty()
		ai_settings.increase_speed()

		stats.level += 1
		sb.prep_level()
		create_fleet(ai_settings,screen,ship,aliens)


def check_keydown_events(event,ai_settings,screen,ship,bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		#飞船右移动
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		#飞船左移动
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		#飞船上移动
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		#飞船下移动
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		# 开火
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()
		

def fire_bullet(ai_settings,screen,ship,bullets):
	#判断子弹数
	if len(bullets) < ai_settings.bullets_allowed:
		#创建一颗子弹 并加入到编组bullets中
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)


def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		#飞船上移动
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		#飞船下移动
		ship.moving_down = False


def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets):
	"""响应按键和鼠标事件"""
	#监听键盘和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)

		elif event.type  == pygame.MOUSEBUTTONDOWN:
			mouse_x ,mouse_y = pygame.mouse.get_pos()

			check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):

	button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		if play_button.rect.collidepoint(mouse_x,mouse_y):
			#重置游戏
			ai_settings.initialize_dynamic_settings()

			pygame.mouse.set_visible(False)
			#重制游戏
			stats.reset_stats()

			stats.game_active = True		

			aliens.empty()
			bullets.empty()

			create_fleet(ai_settings,screen,ship,aliens)
			ship.center_ship()

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
	"""更新屏幕上的图像，并切换到新屏幕"""
	#每次循环的时候都重绘屏幕
	screen.fill(ai_settings.bg_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	aliens.draw(screen) #调用draw pygame 回自动绘制编组的每个元素 

	sb.show_score()

	#如果游戏处于非活动状态9⃣️绘制按钮
	if not stats.game_active:
		play_button.draw_button()

	#让最近绘制屏幕可见
	pygame.display.flip()