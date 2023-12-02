import matplotlib.pyplot as plt
import numpy as np
def graph_plot():

    X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    xpoints =np.random.choice(X, 15)
    plt.subplot(2, 1, 1)
    plt.plot(xpoints, ms = 10, mec = 'b', mfc = 'w', linestyle = '-.', linewidth = '1.5')
    plt.title("Mt Graph", loc = 'right')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(axis = 'y', color = 'red', linestyle = ':', linewidth = 2.5)
    plt.subplot(2, 1, 2)
    plt.title("My Graph", loc = 'left')
    plt.plot(xpoints, ms = 10, mec = 'g', mfc = 'w', linestyle = '-.', linewidth = '1.5')
    plt.suptitle("MY Graphs")

    plt.show()
def graph_scatter():
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
    sizes = 10 * np.random.randint(100, size=(13))
    plt.scatter(x, y, c=colors, cmap='tab20_r', s=sizes, alpha=0.3)
    plt.colorbar()
    plt.show()
def graph_bar():
    x = np.array(["sunday", "monday", "thuseday", "wednsday"])
    y = np.array([3, 8, 1, 10])

    plt.bar(x,y, color = "red", width =0.5)
    plt.show()
def graph_bar():
    x = np.random.normal(170, 10, 10)

    plt.hist(x)
    plt.show()
y = np.array([35, 25, 25, 15, 2, 45, 67])
mylabels = ["1", "2", "3", "4", "5", "6", "7"]
myexplode = [0.2, 0, 0, 0, 1, 0, 0.9]
plt.pie(y, labels=mylabels, startangle = 180, explode = myexplode, shadow = True)
plt.legend(title = "seven numbers:")
plt.show()