# https://leetcode.com/problems/global-and-local-inversions/
class Solution:
    def isIdealPermutation(self, nums) -> bool:
        i = 0
        n = len(nums)
        c = 0
        while i + 1 < n:
            if nums[i] > nums[i + 1]:
                c += 1
            i += 1
        g = self.inversionCount(nums, 0, len(nums) - 1)
        return g == c

    def inversionCount(self, arr, low, high):
        if high - low + 1 == 1:
            return 0

        else:
            mid = low + (high - low) // 2
            x = self.inversionCount(arr, low, mid)
            y = self.inversionCount(arr, mid + 1, high)
            z = self.countActual(arr, low, mid, high)
            return x + y + z

    def countActual(self, arr, low, mid, high):
        invCount = 0
        res = []
        a1 = arr[low: mid + 1]
        a2 = arr[mid + 1: high + 1]
        i, j = low, mid + 1

        while i < mid + 1 and j < high + 1:
            if arr[i] <= arr[j]:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1
                invCount += mid - low - i

        while i < len(a1):
            res.append(a1[i])
            i += 1

        while j < len(a2):
            res.append(a2[j])
            j += 1

        arr[low:high + 1] = res

        return invCount


if __name__ == '__main__':
    so = Solution()
    arr = [1, 0, 2]
    out = so.isIdealPermutation(arr)
    print(out)
