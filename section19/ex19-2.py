import matplotlib.pyplot as plt
figure = plt.figure()
axes = figure.add_subplot(111)

noise = list(range(20, 71, 5))
stress = [10, 11, 15, 20, 30, 42, 55, 70, 88, 110, 150]

axes.scatter(noise, stress, s = noise, c = noise)

plt.show()