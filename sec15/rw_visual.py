import matplotlib.pyplot as plt 
from random_walk import RandomWalk

#只要程序处于活跃状态就不懂的模拟随机漫步
while True:

	rw = RandomWalk(50000)
	rw.fill_walk()
	# plt.scatter(rw.x_value,rw.y_value,s=15)
	# plt.show()

	#设置绘图窗口
	plt.figure(figsize=(12,6))

	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_value,rw.y_value,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=1)

	#重新绘制起点和终点
	plt.scatter(0,0,c='green',edgecolor='none',s=100)
	plt.scatter(rw.x_value[-1],rw.y_value[-1],c='red',edgecolor='none',s=100)

	#隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	break