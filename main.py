# Week 5

# ==============================================================
# Question 1
# ============
''' Write a function f, that takes a set of numbers as its singe
    parameter and returns a list containing the same numbers,
    sorted into descending order '''


def f(num):
    lst = []
    for x in num:
        lst.append(x)
    lst.sort(reverse=True)
    return lst


z = {2, 9, 4}
print(f(z))


def f2(num):
    lst = f(num)

    t = tuple(lst)
    return t


z = {2, 9, 4}
print(f2(z))
# ===========================================================
# Question 2
# ============
''' Write a function Combine that takes two lists of
    the same length, a and b, as parameters and
    returns a list of pairs as its result. Each pair
    in the result list should contain an element from
    a and an element from b, such that
    result [i] is (a[i],b[i]). '''


def Combine(a, b):
    result = []
    for x in range(len(a)):
        s = set()
        s.add(a[x])
        s.add(b[x])
        result.append(s)

    return result


z = [1, 2, 3]
u = ['a', 'b', 'c']
print(Combine(z, u))

''' Modification: change the function so that it works
    when the lists a and b are of unequal lengths,
    returning a result that is the same length as the
    shorter of a and b '''


def Combine2(a, b):
    if len(a) < len(b):
        lst = Combine(a, b)
        return lst
    if len(a) == len(b):
        lst = Combine(a, b)
        return lst
    if len(a) > len(b):
        lst = Combine(a, b)
        return lst


z = [1, 2]
u = ['a', 'b']
print(Combine2(z, u))

# ===========================================================
# Question 3
# =============
''' Write a function SmallestLHSet that takes a set
    of pairs of numbers as its parameter, and
    returns the pair with the smallest left-hand
    element. If there are two or more pairs that
    could be returned as the result (because they
    have the same left-hand element) the function
    may return any one of them. '''


def SmallestLHSet(pairs):
    lst = list(pairs)
    temp = []
    for x in range(len(lst)):
        element = list(lst[x])
        temp.append(element[0])
    smallestnum = min(temp)

    for x in range(len(lst)):
        element = list(lst[x])
        if smallestnum == element[0]:
            pair = tuple(element)
            return pair


z = {(7, 2), (3, 4), (7, 6), (2, 2)}
print(SmallestLHSet(z))

''' Create a second function SmallestLHList that
    performs the same operation on lists of pairs of
    numbers. If there are two or more pairs that could
    be returned as the result (because they have the
    same left-hand element) the function must return the
    pair that appears earliest in the list. '''


def SmallestLHList2(pairs):
    catch = SmallestLHSet(pairs)


z = [(7, 2), (3, 4), (7, 6), (2, 2)]
print(SmallestLHSet2(z))
''' Create a third function GreatestSumSet that takes
    a set of pairs of numbers and returns the pair
    for which the sum of its elements is greatest.
    If there are two or more possible pairs that could
    be returned as the result (because they have the
    same sum of elements) the function may return any
    one of them '''


def GreatestSumSet(pairs):
    lst = list(pairs)
    temp = []
    for x in range(len(lst)):
        element = list(lst[x])
        tempsum = element[0] + element[1]
        temp.append(tempsum)
    greatestsum = max(temp)

    for x in range(len(lst)):
        element = list(lst[x])
        if greatestsum == element[0] + element[1]:
            pair = tuple(element)
            return pair


z = {(7, 2), (3, 4), (7, 6), (2, 2)}
print(GreatestSumSet(z))
# ===========================================================
# Question 4
# =============
#ok
