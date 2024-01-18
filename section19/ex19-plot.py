import matplotlib.pyplot as plt
figure = plt.figure()

axes = figure.add_subplot(111)
x1 = list(range(5))
y1 = [4, 1, 3, 5, 2]

x2 = list(range(5))
y2 = [0, 8, 5, 3, 1]

axes.plot(x1, y1, linestyle = 'dotted', linewidth = 1)
axes.plot(x2, y2, color = 'g', marker = '^')

plt.show()