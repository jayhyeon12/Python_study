import wordcloud
import matplotlib.pyplot as plt

words = {'파이썬': 10, '빅데이터': 5, '웹 크롤링': 9, '딥러닝': 12}

wc = wordcloud.WordCloud(font_path = r'C:\Windows\Fonts\HMKMMAG.TTF')
cloud = wc.generate_from_frequencies(words)

plt.figure()
plt.imshow(cloud)
plt.show()