def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""

    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        left, right = 0, len(list_of_integers) - 1
        while left < right:
            mid = (left + right) // 2
            if list_of_integers[mid] < list_of_integers[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return list_of_integers[left]


print(find_peak([1, 2, 4, 6, 3])) # 6
print(find_peak([4, 2, 1, 2, 3, 1])) # 4
print(find_peak([2, 2, 2])) # 2
print(find_peak([2, 2])) # 2
print(find_peak([1])) # 1
print(find_peak([])) # None
print(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 10
