"""
ch1.py

Auther: thgch
Created on 2020/05/17

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread


class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("Hello {}!".format(self.name))

    def goodbye(self):
        print("Good-bye {}!".format(self.name))


def draw_graph1():
    x = np.arange(0, 6, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()


def draw_graph2():
    x = np.arange(0, 6, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plt.plot(x, y1, label="sin")
    plt.plot(x, y2, linestyle="--", label="cos")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title('sin & cos')
    plt.legend()
    plt.show()


def draw_img():
    img = imread('lena.png')
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    draw_graph1()
    draw_graph2()
    draw_img()

