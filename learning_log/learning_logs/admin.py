from django.contrib import admin

# Register your models here.
#1导入要注册的模型。 2 注册
from learning_logs.models import Topic,Entry
#2
admin.site.register(Topic)

admin.site.register(Entry)
