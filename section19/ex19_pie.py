# 파이 차트

import matplotlib.pyplot as plt
figure = plt.figure()
axes = figure.add_subplot(111)

data = [6, 5, 3, 7]
label = ['Good', 'Bad', 'Normal', 'Not bad']

axes.pie(data, labels = label, autopct = '%d%%')
plt.axes('equal')
plt.legend(label, loc = 'center right')
plt.show()