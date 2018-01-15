import matplotlib.pyplot as plt
from random import choice
direction = choice([1,-1])
print(direction)
exit(1)

#绘制折线图
input_values = [1,2,3,4,5,6,7,8,9,10]
squares = [1,4,9,16,25,36,49,64,81,100]

plt.plot(input_values,squares,linewidth=5)
plt.show()