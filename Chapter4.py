"""
第四章的练习题：4.3
作者：yaming
时间：2019.3.5
突破点：每个三角形的两边是相同的；利用正多边形进行测试
"""

import math
import turtle


def triangle(f, n, length):
    angle = 180 / n
    for i in range(n):
        f.fd(length)
        f.lt(90 + angle)
        f.fd(2 * length * math.sin(angle/180*math.pi))      # sin函数接受弧度制
        f.lt(90 + angle)
        f.fd(length)
        f.lt(180)


if __name__ == '__main__':
    flower = turtle.Turtle()
    flo_length = 100
    tri_n = 3
    flower.speed(6)
    flower.hideturtle()

    triangle(flower, tri_n, flo_length)

    turtle.mainloop()
