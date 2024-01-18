from matplotlib import font_manager, rc # 차트에서 한글 사용 가능
import matplotlib
import matplotlib.pyplot as plt

font_path = r'C:\Windows\Fonts\HMKMMAG.TTF'

font_name = font_manager.FontProperties(fname = font_path).get_name()

matplotlib.rc('font', family = font_name)

x = ['봄', '여름', '가을', '겨울']
y = [20.5, 30.5, 15.5, 1.5]

plt.plot(x, y)

plt.show()