m = 32
arr = [0] * m


def h(i):
    def f(x):
        s1 = x * x
        s2 = s1 * x
        s = s1 + s2
        s *= i
        return s % m

    return f


def insert(x):
    for i in range(1, 4):
        val = h(i)(x)
        arr[val] = 1


inserts = [2010, 2013]

for x in inserts:
    insert(x)


def out():
    info = [(i, x) for i, x in enumerate(arr) if x == 1]
    print(",".join([str(x[0]) for x in info]))


def does_exist(x):
    for i in range(3):
        val = h(i)(x)
        if arr[val] == 0:
            return False
    return True


out()

insert(2007)
out()
insert(2004)
out()
insert(2001)
insert(1998)

out()
print(does_exist(2004))
print(does_exist(3200))
