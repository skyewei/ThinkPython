import turtle
from math import pi

bob = turtle.Turtle()   # 由turtle模块创建一个Turtle对象，并指向bob
turtle.setup(1200, 1000, 0, 0)

# 4.3.1 square函数绘制正方形
# def square(test, length):
#     """ 绘制正方形"""              # 文档字符串（三重引号字符串），也叫多行字符串，函数的关键信息、函数的作用、形参的作用等，在开发中较为重要，可参看官方文档。
#     for i in range(4):
#         test.fd(length)
#         test.lt(90)
# chang = int(input('please enter the length: '))
# square(bob, chang)


# 4.3.3 polygon函数绘制正n边形
# def polygon(test, length, n):
#     """ 绘制正n边形"""
#     for i in range(n):
#         test.fd(length)
#         test.lt(360/n)
# polygon(bob, length = 60, n = 16)


# my_idea——利用圆来绘制正n边形
# bob.circle(100, 360, 6)


# 4.3.4利用正N边形来绘制近似圆
# def polygon_cir(test, length, n):
#     """ 绘制正n边形"""
#     for i in range(n):
#         test.fd(length)
#         test.lt(360/n)


# def circle(test1, r):
#     """ 调用polygon()函数，画近似圆"""
#     polygon_cir(test1, 2*3*10*r/16, 16)
# circle(bob, 10)


# # 泛化"正N边形写圆" 函数——在上面的函数中，n是固定的，对画不同的圆会浪费资源，故将n改写成约为周长的1/3左右，提高效率！
# def polygon_cir_re(test, length, n):
#     """ 绘制正n边形"""
#     for i in range(n):
#         test.fd(length)
#         test.lt(360/n)
#
#
# def circle_re(test1, r):
#     """ 调用polygon()函数，画近似圆"""
#     circus = pi * 2 * r
#     n = int(circus / 3) + 1             # 将n也随着圆的大小变化，但大约是周长的1/3.
#     length = circus / n
#     polygon_cir_re(test1, length, n)
#
# circle_re(bob, 50)
# turtle.done()           # 海龟结束爬行


# 4.3.5 更为泛化的circle函数(arc函数)，额外的参数angle，可以画更为完整的圆
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


# def polygon(t, n, length):
#     angle = 360.0 / n
#     polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    arc(t, r, 360)

circle(bob, 60)
bob.hideturtle()
# bob.circle(60)    为什么采用对象方式和导入库的函数调用不同？？？
turtle.done()


## if __name__ == '__main__':
