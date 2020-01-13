## 习题15.2

import turtle


class Rectangle:
    """ attributes: the left start point, the wide and height."""
class Point:
    """ x and y"""
class Circle:
    """Represent a circle.
    Attributes: the center point and radius."""

def draw_circle(t, c):
    t.up()
    t.goto(c.center.x, c.center.y-c.radius)     ## circle begin the start point not the center point.
    t.down()

    t.circle(c.radius)


def draw_rec(t, p):
    t.up()
    t.goto(p.left.x, p.left.y)
    t.down()

    for i in range(2):
        t.fd(p.wide)
        t.lt(90)
        t.fd(p.height)
        t.lt(90)

def main():

    bob = turtle.Turtle()
    rec = Rectangle()
    cir = Circle()

    rec.left = Point()
    rec.left.x = 50.0
    rec.left.y = 50.0
    rec.wide = 100.0
    rec.height = 200.0

    cir.center = Point()
    cir.center.x = 120.0
    cir.center.y = 120.0
    cir.radius = 5.0

    bob.hideturtle()        ## make the bob turtle object invible.
    draw_rec(bob, rec)
    draw_circle(bob, cir)

    turtle.mainloop()


main()