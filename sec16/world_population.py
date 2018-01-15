import json
from country_codes import get_country_code
from pygal.style import RotateStyle
import pygal

filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

cc_populations = {}
#打印
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict["Country Name"]
		popution = int(float(pop_dict["Value"]))
		code = get_country_code(country_name)
		if code:
			cc_populations[code]=popution


#根据人口数量分组1 少于1000w。  1000w-10亿。  10亿以上
cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
for cc,pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop

wm_style = RotateStyle('#336699')
wm = pygal.Worldmap(style=wm_style)

wm.title = "world popution in 2010,by country"

wm.add('2010 0-10m',cc_pops_1)
wm.add('2010 10m-1bn',cc_pops_2)
wm.add('2010 >1bn',cc_pops_3)

wm.render_to_file('world_populations.svg')