import sys

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


def solve():
    # <<<START>>>


if __name__ == "__main__":
    solve()
