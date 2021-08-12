class Solution:
    calls = 0
    pivot = None
    call_array = []

    def __init__(self, use=False, high=False, low=False):
        self.high = high
        self.useMedian = use
        self.low = low

    def partition(self, arr, pivot_index):
        if pivot_index != 0:
            arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
            pivot_index = 0

        last_seen_small = 0
        unseen = 1

        pivot = arr[pivot_index]
        while unseen < len(arr):
            elem = arr[unseen]
            if elem >= pivot:
                unseen += 1
            else:
                temp = unseen
                while temp > last_seen_small + 1:
                    arr[temp] = arr[temp - 1]
                    temp -= 1
                arr[temp] = elem
                last_seen_small += 1
                unseen += 1

        arr[last_seen_small], arr[pivot_index] = arr[pivot_index], arr[last_seen_small]
        return last_seen_small, arr[last_seen_small]

    def partition_lecture(self, arr, pivot_index):
        arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
        pivot = arr[0]
        r = len(arr)
        i = 1
        for j in range(1, r):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[0], arr[i - 1] = arr[i - 1], arr[0]
        return i - 1, arr[i - 1]

    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr

        if self.high:
            pivot_index = len(arr) - 1
        elif self.low:
            pivot_index = 0
        else:
            pivot_index = self.chooseMedianAsPivot(arr)

        p, pivot = self.partition_lecture(arr, pivot_index=pivot_index)
        arr[:p] = self.quickSort(arr[: p])
        arr[p + 1:] = self.quickSort(arr[p + 1:])

        self.calls += len(arr) - 1

        return arr

    def chooseMedianAsPivot(self, arr):
        n = len(arr)
        first = arr[0]
        final = arr[-1]
        mid_index = n // 2 if n % 2 == 1 else (n // 2) - 1
        middle = arr[mid_index]
        A = [(first, 0), (middle, mid_index), (final, n - 1)]
        mx = max(A, key=lambda x: x[0])[0]
        mn = min(A, key=lambda x: x[0])[0]
        for i in range(3):
            if A[i][0] != mx and A[i][0] != mn:
                return A[i][1]
        return n - 1


if __name__ == '__main__':

    def run(flag, label):
        f = r'C:\Users\anime\PycharmProjects\PyDSA\courseraStanford\DivideAndConquer\Week3\sketch.txt'
        g = r'C:\Users\anime\PycharmProjects\PyDSA\courseraStanford\DivideAndConquer\Week3\QuickSort.txt'
        f = g
        with open(f) as f:
            x = f.readlines()
        arr = [int(y.rstrip()) for y in x]
        if flag == "use":
            so = Solution(use=True)
        elif flag == "low":
            so = Solution(low=True)
        elif flag == "high":
            so = Solution(high=True)
        sorted_arr = sorted(arr)
        so.quickSort(arr)
        print(arr == sorted_arr)
        print(label, " ", so.calls)


    for flag, label in [("low", "low"), ("high", "high"), ("use", "Median")]:
        run(flag, label)

    print(" ")
