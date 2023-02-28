import math

#EXERCISE 7-1 - Calculating square roots


def mysqrt(a):
    """
    Calculates the square root of a provided integer

    :param a: int - number to take the square root of
    :return: float - the square root of a
    """

    x = float(a - 1)
    y = float(1)

    while abs(y - x) > .000000001:
        x = y
        y = (x + a/x)/2

    return(y)

# print("a\tmysqrt(a)\tmath.sqrt(a)\tdiff")
# print('-   ---------   ------------   --------')
#
# for i in range(9):
#     a = i + 1
#     print(a, '\t',
#           mysqrt(a), '\t',
#           math.sqrt(a), '\t',
#           abs(mysqrt(a) - math.sqrt(a)))


# EXERCISE 7-3 - Calculating 1/pi in a loop

def estimate_pi():
    """
    This function uses Srinivasa Ramanujan's approximation to estimate 1/pi

    :return: float - the approximation of 1/pi
    """
    x = 1
    k = 0

    while x > 1e-15:
        numerator = math.factorial(k * 4) * (1103 + 26390 * k)
        denominator = math.factorial(k) ** 4 * 396 ** (4 * k)

        x = numerator/denominator
        k += 1

    multiplier = (2 * math.sqrt(2)) / 9801

    result = x * multiplier

    return result


print(estimate_pi())
print(1 / math.pi)