import csv
import matplotlib.pyplot as plt
from datetime import datetime
# sitka_weather_2014.csv
#sitka_weather_07-2014.csv
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	#next 处理一行 并以逗号分隔，存入列表中
	header_row = next(reader)


	# for index , column_header in enumerate(header_row):
	# 	print(index,column_header)


	dates,highs,lows = [],[],[]
	for row in reader:
		# current_date = datetime.strptime(row[0],"%Y-%m-%d")
		current_date = datetime.strptime(row[0],"%Y-%m-%d")
		dates.append(current_date)

		high = int(row[1])
		highs.append(high)

		low = int(row[3])
		lows.append(low)
	# print(dates)
	# print(highs)

	#根据数据绘制图形

fig = plt.figure(dpi=128,figsize=(12,6))
plt.plot(dates,highs,c="red",alpha=0.5)
plt.plot(dates,lows,c="blue",alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='orange',alpha=1)

plt.title("daily high and low temperatures,july 2014" , fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("temperature(F)",fontsize=16)
plt.tick_params(axis='both',which="major",labelsize=16) #设定样式。 
plt.show()