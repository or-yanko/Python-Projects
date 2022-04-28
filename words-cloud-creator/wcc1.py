from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
import os

a = open(str(os.getcwd())+ '/txt.txt', 'r').read()

wc = WordCloud().generate(a)
plt.imshow(wc)
plt.axis("off")
plt.show()