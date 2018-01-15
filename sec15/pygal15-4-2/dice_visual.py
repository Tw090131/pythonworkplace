from die import Die
import pygal

#创建2个骰子
die_1 = Die()
die_2 = Die()
#丢几次骰子 并将结果存储在一个列表中
results = []
for roll in range(10000):
	result = die_1.roll()+die_2.roll()
	results.append(result)
# print(results)

#分析结果
frequencies = []
max_result = die_1.num_sides+die_2.num_sides
for value in range(1,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# print(frequencies)

#对结果进行可视化
#创建条形图
hist = pygal.Bar()

hist.title = "results of rolling one d6 10000 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "result"
hist.y_title = "times"

hist.add('D6 + D6',frequencies)
hist.render_to_file('dice_visual.svg')


