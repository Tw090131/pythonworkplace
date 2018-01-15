import pygal

wm = pygal.Worldmap()
wm.title = "north , central , and south america"

wm.add('north america', ['ca','mx','us'])
wm.add('central america',['bz','cr','gt','hm','ni','pa','sv'])
wm.add('south america',['ar','bo','br','cl','gf'])

wm.render_to_file('americas.svg')