import sys
import itertools as it
from bisect import bisect_left as bsl
from bisect import bisect_right as bsr


read = sys.stdin.readline
write = sys.stdout.write

newl="\n"
space=" "
empty=""

MOD = 10**9 + 7


def get(T=int):
    return T(read().strip())


def getarr(T=int):
    return list(map(T, read().strip().split()))


def put(s, sep=newl):
    write(str(s) + sep)


def putarr(group, sep=space, end=newl):
    for item in group:
        put(item, sep)
    write(end)


# <<<START>>>




































































