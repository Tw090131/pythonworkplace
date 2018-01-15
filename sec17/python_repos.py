import requests
import pygal
from pygal.style import LightColorizedStyle as LCS ,LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print('code: ',r.status_code)

response_dict = r.json()

print(response_dict.keys())

print("total repositories: ",response_dict['total_count'])

#研究有关仓库的信息
repo_dicts = response_dict['items']

names,stars = [],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

#可视化
my_style = LS("#333366",base_style=LCS)
#让标签绕着x轴旋转45度，并隐藏了图例
chart = pygal.Bar(style=my_style,x_label_rotation=90,show_legend=False)
chart.title='most stared python projects on github'
chart.x_labels = names
chart.add('python',stars)
chart.render_to_file('python_repos.svg')

# print("repositories returned: " ,len(repo_dicts))



# #研究第一个仓库
# repo_dict = repo_dicts[0]
# print(repo_dict)
# print("\nkeys: ",len(repo_dict))
# for key in sorted(repo_dict.keys()):
# 	print(key)


