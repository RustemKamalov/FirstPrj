import itertools


def primes():
    s = 1
    lst = []
    while True:
        s += 1
        for j in lst:
            if s % j == 0:
                break
        else:
            lst.append(s)
            yield s


print(list(itertools.takewhile(lambda x : x <= 31, primes())))
