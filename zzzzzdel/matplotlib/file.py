import matplotlib
import matplotlib.pyplot as plt #רוב כלי השירות של Matplotlib נמצאים תחת תת-מודול ה-pyplot, ובדרך כלל מיובאים תחת הכינוי plt:
import numpy as np #בעזרת התקיה הזאתי יוצרים רשימה של נקודות איקס וווי שנוכל להכניס לגרף שלנו
ypoints = np.array([3, 8, 1, 10])

def get_matplotlib_version():
    print("matplotlib version:",matplotlib.__version__)


#משתנה ראשון הוא רשימה של איקס
#משתנה ראשון הוא רשימה של איקס

def draw_graph_from_np_arrays(array_x_points =np.array([]) ,array_y_points=np.array([]), option=''):
    plt.plot(array_x_points, array_y_points,option)# מצייר את הרשימה, במידה ושמים רק רשימה אחת, מתייחס לזה כנקודות ווי ברווחים שונים
    plt.show()
#draw_graph_from_np_arrays(np.array([1, 2, 6, 8]),np.array([3, 8, 1, 10]))#draw graph with line
#draw_graph_from_np_arrays(np.array([1, 2, 6, 8]),np.array([3, 8, 1, 10]),'o')#draw graph only dots
#draw_graph_from_np_arrays()#draw it blank


#אם תוסיף מרקר ואחרי זה את האות 0 זה יראה לנו רק נקודות 
def d1():# draw graph with lime and dots
    plt.plot(ypoints, marker = 'o')
    plt.show()  
#
# כל האופציות הקיימות לסגנון הנקודות בקישור מתחת
# https://www.w3schools.com/python/matplotlib_markers.asp
#

#אם תוסיף מרקר * זה יוסיף גם כוכביות במקום נקודות וגם קו
def d2():
    plt.plot(ypoints, marker = 'r')
    plt.show()

x = np.random.normal(170, 10, 250)
print(x)
plt.hist(x)
plt.show() 
