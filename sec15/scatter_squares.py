import matplotlib.pyplot as plt


# plt.scatter(2,4,s=200)


# x_value = [1,2,3,4,5]
# y_value = [1,4,9,16,25]

# plt.scatter(x_value,y_value,s=100)

# #设置图标标题并给坐标轴加上标签
# plt.title("square numbers",fontsize=24)
# plt.xlabel("value",fontsize=24)
# plt.ylabel("square of value",fontsize=24)

# #设置刻度标记的大小
# plt.tick_params(axis='both',which="major",labelsize=24)

# plt.show()



#自动计算坐标
x_values = list(range(1,101))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values,y_values,c='red',edgecolor='none',s=40)
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)

#设置图标标题并给坐标轴加上标签
plt.title("square numbers",fontsize=24)
plt.xlabel("value",fontsize=24)
plt.ylabel("square of value",fontsize=24)

#设置每个坐标轴的取值范围
plt.axis([0,111,0,11000])

#画图
# plt.show()

#保存
plt.savefig('squares_plot.png',bbox_inches='tight')



