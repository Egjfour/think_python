

# EXERCISE 10-1: Nested sums of lists


def nested_sum(t):
    """
    Calculates the sum of nested list elements

    :param t: list - the list of elements to find the sum of
    :return: float - sum of the list elements
    """

    total = 0

    for e in t:
        total += sum(e)

    return total


# EXERCISE 10-2: Cumsum of list


def cumsum(t):
    total = 0

    cumsum_list = []
    for e in t:
        total += e
        cumsum_list.append(total)

    return cumsum_list


# EXERCISE 10-3 and 10-4: returns all but the first and last elements


def middle(t):
    return t[1:-1]


def chop(t):
    del t[0]
    del t[-1]

    return None


# EXERCISE 10-5: Checks if a list is sorted ascending


def is_sorted(t):
    copy_t = t.copy()
    copy_t.sort()
    return t == copy_t


# EXERCISE 10-6: Checking for anagrams


def is_anagram(s1, s2):
    str_list1 = list(s1.lower())
    str_list2 = list(s2.lower())

    str_list1.sort()
    str_list2.sort()

    return str_list1 == str_list2


