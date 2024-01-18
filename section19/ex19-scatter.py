# 산포도 그래프

import matplotlib.pyplot as plt
figure = plt.figure()
axes = figure.add_subplot(111)

x = list(range(1, 7))
y = [1, 2, 4, 5, 7, 6]

area = [50, 100, 150, 200, 250, 300]
color = ['red', 'green', 'blue', 'navy', 'aqua', 'crimson']
axes.scatter(x, y, s = area, c = color)

plt.show()