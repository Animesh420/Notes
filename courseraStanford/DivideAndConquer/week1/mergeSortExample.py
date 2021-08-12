class Solution:
    def mergeSort(self, arr, low, high):
        if low < high:
            mid = low + (high - low) // 2
            self.mergeSort(arr, low, mid)
            self.mergeSort(arr, mid + 1, high)
            self.merge(arr, low, mid, high)

    def merge(self, arr, low, mid, high):
        res = []
        a1 = arr[low: mid + 1]
        a2 = arr[mid + 1: high + 1]

        i = 0
        j = 0

        while i < len(a1) and j < len(a2):

            if a1[i] <= a2[j]:
                res.append(a1[i])
                i += 1
            else:
                res.append(a2[j])
                j += 1

        while i < len(a1):
            res.append(a1[i])
            i += 1

        while j < len(a2):
            res.append(a2[j])
            j += 1

        arr[low:high + 1] = res


if __name__ == '__main__':
    so = Solution()
    arr = [14, 23, 3, 1, - 9, 15, 12, 47]
    sorted_arr = sorted(arr)
    print(sorted_arr)
    so.mergeSort(arr, 0, len(arr) - 1)
    print(arr)
    print(arr == sorted_arr)
