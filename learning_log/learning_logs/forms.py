from django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):
	class Meta:
		"""meta 告诉django 用那个魔性创建表单"""
		model = Topic
		#该表单只包含text 的字段
		fields = ['text']
		#不要为字段text 生成标签
		labels = {'text':''}

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text':''}
		widgets = {'text':forms.Textarea(attrs={'cols':80})}


