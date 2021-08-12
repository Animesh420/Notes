f = r'C:\Users\anime\PycharmProjects\PyDSA\courseraStanford\DivideAndConquer\Week3\QuickSort.txt'
g = r'C:\Users\anime\PycharmProjects\PyDSA\courseraStanford\DivideAndConquer\Week3\sketch.txt'
g = f
with open(g) as f:
    a = [int(x) for x in f]


def FindMedian(A):
    minvalue = min(A)
    maxvalue = max(A)
    for i in range(3):
        if A[i] != minvalue and A[i] != maxvalue:
            return A[i]


def ChoosePivot(A, flag):
    n = len(A)
    first = A[0]
    final = A[n - 1]
    k = (n // 2) if n % 2 == 1 else (n // 2) - 1
    middle = A[k]

    B = [first, middle, final]
    med = FindMedian(B)
    if med == B[0]:
        position = 0
    elif med == B[1]:
        position = k
    else:
        position = n - 1

    if flag == 1:
        return 0
    if flag == 2:
        return n - 1
    if flag == 3:
        return position
    else:
        pass


def Swap(A, first, second):
    A[first], A[second] = A[second], A[first]
    return A


def Partition(A):
    pivot = A[0]
    r = len(A)
    i = 1
    for j in range(1, r):
        if A[j] < pivot:
            A = Swap(A, i, j)
            i += 1
    A = Swap(A, 0, i - 1)
    return A, i - 1


call_array = []


def QuickSort(A, flag):
    n = len(A)
    if n > 1:
        p = ChoosePivot(A, flag)
        A = Swap(A, 0, p)
        A, pivot_position = Partition(A)
        A[:pivot_position], left = QuickSort(A[:pivot_position], flag)
        A[pivot_position + 1:], right = QuickSort(A[pivot_position + 1:], flag)
        call = left + right + n - 1
    else:
        call = 0
    return A, call


if __name__ == '__main__':
    so = sorted(a)
    for flag, label in [(1, "low"), (2, "high"), (3, "median")][::-1]:
        s, c = QuickSort(a.copy(), flag)
        print(s == so, label, c)
