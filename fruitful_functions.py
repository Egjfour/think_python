import math


# EXERCISE 6-1 - draw a stack diagram to find the answer. Found the correct answer of 8100 before checking
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod


def a(x, y):
    x = x + 1
    return x * y


def c(x, y, z):
    total = x + y + z
    square = b(total) ** 2
    return square


x = 1
y = x + 1
print(c(x, y + 3, x + y))


# EXERCISE 6-2: Write the ackerman function


def ack(m, n):
    """
    returns the result of the ackerman function
    n + 1 if m == 0
    ack(m-1, 1) if m > 0 and n = 0
    ack(m - 1, ack(m , n - 1)) if m > 0 and n > 0

    :param m: int - one of the values to use for calculating
    :param n: int - the other value to use for calculating
    :return: int - the result of the Ackerman function
    """

    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))


print(ack(3, 4))


# EXERCISE 6-3 - testing palindromes


def is_palindrome(word):
    """
    Checks if a provided word is a palindrome
    This means it is the same spelled forward or backward

    :param word: string - the word to evaluate as a palindrome
    :return: bool - whether the word is a palindrome
    """

    first_letter = word[0]
    last_letter = word[-1]
    middle_letters = word[1:-1]

    if first_letter != last_letter:
        return False
    if len(middle_letters) == 1:
        return True
    else:
        return is_palindrome(middle_letters)


print(is_palindrome('racecar'))
print(is_palindrome('battleship'))


# EXERCISE 6-4 - Evaluating if one number is a power of another


def is_power(a, b):
    """
    Checks if the integer a is a power of the interger b

    :param a: int - the number to check if it is a power of param b
    :param b: int - the number to use to verify a
    :return: bool - whether a is a power of b
    """

    if a == b:
        return True

    if a % b != 0:
        return False
    else:
        return is_power(a / b, b)


print(is_power(27, 3))
print(is_power(27, 4))


# EXERCISE 6-5 - Finding The Greatest Common Denominator


def gcd(a, b):
    """
    Finds the greatest common denominator between two provided numbers

    :param a: int - first number provided
    :param b: int - second number provided
    :return: int - the greatest common denominator between the two numbers
    """

    if b == 0:  # from the fact that gcd(a, 0) = a
        return a
    else:
        remainder = a % b
        return gcd(b, remainder)


print(gcd(148, 36))
