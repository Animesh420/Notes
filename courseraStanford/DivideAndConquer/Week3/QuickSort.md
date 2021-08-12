Quicksort:
1. Average run time is O(nlogn)
2. This is inplace, requires very less space to run

General Pseudocode:
1. Pick a pivot element
2. Partition the array such that all elements to left of pivot are smaller than pivot and all element to the right of the pivot are greater than the pivot.
3. The pivot element ends at being its rightful position.
4. Partition subroutine is O(N) and O(1) space.
5. Pseudocode:
    def quickSort(arr, n):
        if n == 1:
        return arr 
        else:
           pivot = choose_pivot(arr, n)
           partition(arr, n, pivot)
           mid = n // 2
           quickSort(0, mid)
           quickSort(mid + 1, n)
6. Paritioning function:
    1. A poor implementation:
        1. Take a O(N) memory and do the following.
        2. Keep two pointes front and back. pointing to an array start and end.
        3. if you meet an element less than pivot write to front and increment front
        4. if you meet an element more than pivor write to back and decrement back
        5. After you have traversed the array, write pivot to front or back, both of them should be equal by now.
        
    2. In place implementation:
        1. We implement the partition routine and get the pivot element
        2. recurse of elements less than position of pivot and elements greater than position of pivot.