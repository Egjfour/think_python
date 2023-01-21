import time
import datetime
import math
import turtle

bob = turtle.Turtle()

# Exercise 5-1
current_time = time.time()

my_time = datetime.datetime.fromtimestamp(current_time).strftime('%c')

print(my_time)

days_since_start = math.floor(current_time / 60 / 60 / 24)

print(days_since_start)


# EXERCISE 5-2
def check_fermat(a, b, c, n):
    """
    checks to see if fermat's theorem holds for a set of numbers and an exponent
    a^n + b^n = c^n should never be true for any value of n greater than 2

    :param a: first numeric in equation
    :param b: second numeric in equation
    :param c: third numeric in equation
    :param n: number to exponentiate all parameters by
    :return: string - a statement on the success of fermat's theorem
    """

    if n <= 2:
        raise Exception("n must be greater than 2")

    if a ** n + b ** n == c ** n:
        return 'Holy smokes, Fermat was wrong!'
    else:
        return 'No, that doesn\'t work.'


# nums = input("What are the numbers you would like to check for a, b, c, and n (comma-separated list)?\n")
#
# nums_list = list(map(int, nums.split(',')))
# print(check_fermat(nums_list[0], nums_list[1], nums_list[2], nums_list[3]))

# EXERCISE 5-3
def is_triangle(stick1, stick2, stick3):
    """
    Checks to see if the lengths of three sticks (inputs) are able to form a closed triangle.
    It does this by seeing if the sums of lengths any 2 sticks are less than the length of the third.

    :param stick1: float - length of the first stick
    :param stick2: float - length of the second stick
    :param stick3: float - length of the third stick
    :return: string - statement on whether a triangle can be formed
    """

    sums = [stick1 + stick2, stick2 + stick3, stick1 + stick3]

    for val in sums:
        if val < stick1 or val < stick2 or val < stick3:
            return 'Not a triangle'

    return 'Yes, this is a triangle'


# EXERCISE 5-4 -- correctly identified that it would print 6 before running here
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)


recurse(3, 0)


# EXERCISE 5-5: Goal was to guess what this draws. I thought it would be a spiral. That was not correct
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n - 1)
    t.rt(2 * angle)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(length * n)

# EXERCISE 5-6
def draw_koch(t, length):
    """
    Recursively draws a koch curve using a provided turtle object and a given length

    :param t: a turtle object to use for drawing
    :param length: the length for the entire koch curve
    :return: null - draws a turtle object
    """
    if length < 3:
        t.fd(length)
        return
    draw_koch(t, length / 3)
    t.lt(60)
    draw_koch(t, length / 3)
    t.rt(120)
    draw_koch(t, length / 3)
    t.lt(60)
    draw_koch(t, length / 3)

draw_koch(bob, 90)

# draw(bob, 5, 8)
turtle.mainloop()
