import turtle
import math
bob = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    return t

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
def polygon(t, length, n):
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t, r):
    arc(t, r, 360)

## EXCERCISE 4-2
def flower(t, r, angle, num_petals):
    """
    This function uses the arc function in a loop to draw a flower
    given the number of petals, radius, and angle size of the flower arcs

    :param t: turtle object
    :param r: radius of the circle
    :param angle: interior angle
    :param num_petals: number of petals to draw
    :return: NULL - draws on the turtle object
    """
    petal_shift = 360.0/(num_petals + 1)
    for i in range(num_petals + 1):
        arc(t, r, angle*2)
        t.lt(petal_shift)

def pies(t, length, num_pieces, initial_shift):
    """

    :param t: a turtle object to perform the action on
    :param length: length of each side of the piece of the pie
    :param num_pieces: number of pieces of the pie to draw
    :param initial_shift: number of degrees to shift the starting axis
    :return: NULL - draws on the turtle object provided
    """
    interior_angle = 60
    t.lt(initial_shift)
    for i in range(num_pieces + 1):
        polygon(t, length, 3)
        t.lt(interior_angle)

pies(bob, 75, 7, 30)
turtle.mainloop()
