"""定义learning_logs 的url 模式"""

from django.conf.urls import url
from django.urls import path
from . import views

#这句不加回报错
app_name = 'learning_logs'

urlpatterns = [
	#主页
	path(r'' , views.index , name='index'),

	#显示所有的主题
	path(r'topics/',views.topics,name='topics'),

	#特定主题的详情页面
	path(r'topics/<int:topic_id>/',views.topic,name='topic'),

	#添加主题页面
	path(r'new_topic/',views.new_topic,name='new_topic'),

	#添加新条目页面
	path(r'new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),

	#编辑条目页面
	path(r'edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
]