from matplotlib import font_manager, rc # 차트에서 한글 사용 가능
import matplotlib
import matplotlib.pyplot as plt

font_path = r'C:\Windows\Fonts\HMFMMUEX.TTC'

font_name = font_manager.FontProperties(fname = font_path).get_name()
matplotlib.rc('font', family = font_name)

figure = plt.figure()
axes = figure.add_subplot(111)

data = [0.18, 0.3, 3.33, 3.75, 0.38]
label = ['비타민A', '비타민B1', '비타민B2', '나이아신', '비타민B6']
axes.pie(data, labels = label, autopct = '%.1f%%')
plt.axis('equal')
plt.legend(label, loc = 'upper right')
plt.show()