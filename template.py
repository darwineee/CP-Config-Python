import sys
import itertools as it
from bisect import bisect_left as bsl
from bisect import bisect_right as bsr


read = sys.stdin.readline
write = sys.stdout.write

newl="\n"
space=" "


def get(T=int):
    return T(read())


def getarr(T=int):
    return list(map(T, read().split()))


def put(s, sep=newl):
    write(str(s) + sep)


def putarr(group, sep=space, end=newl):
    for item in group:
        put(item, sep)
    write(end)


# <<<START>>>
