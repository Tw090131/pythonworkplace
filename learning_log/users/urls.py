"""为应用程序users 定义url 模式"""

from django.urls import path
from . import views
from django.contrib.auth.views import login
#这句不加回报错
app_name = 'users'

urlpatterns = [
	#登陆页面
	#使用login。代替views.login  表示用默认视图而不是自定义视图。  然后传递字典 告诉django 去哪里找模版
	path(r'login/',login,{'template_name':'users/login.html'},name='login'),

	#注销
	path(r'logout/',views.logout_view,name='logout'),

	#注册页面
	path(r'register/',views.register,name='register'),
]