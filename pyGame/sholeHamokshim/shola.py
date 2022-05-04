import sys
from game import Game


def main():
    g = Game((10, 10), 0.5)
    try:

        size = int(sys.argv[1]), int(sys.argv[2])
        prob = float(sys.argv[3])
        g = Game(size, prob)
    except:
        print('Type instead: \" python shola.py 10 10 0.2 \"')
        exit()
    g.run()


if __name__ == '__main__':
    main()
