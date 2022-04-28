from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
import os

a = open(str(os.getcwd())+ '/txt.txt', 'r').read()

mask1 = np.array(PIL.Image.open(str(os.getcwd())+ '/flower.jpg'))

wc = WordCloud(stopwords=['and','a','is','the'],
                mask=mask1,
                background_color='white',
                #contour_color='black',
                #contour_width=3,
                min_font_size=3,
                #max_words=80 
                ).generate(a)
plt.imshow(wc)
plt.axis("off")
plt.show()