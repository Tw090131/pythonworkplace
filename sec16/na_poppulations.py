import pygal

wm = pygal.Worldmap()
wm.title = "populations of countries in north america"

wm.add("north america",{'ca':234234234,'us':32234234,'mx':111111111})

wm.render_to_file('na_populations.svg')