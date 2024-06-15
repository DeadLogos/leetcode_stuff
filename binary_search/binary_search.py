def left_bound(arr, elem):
    left, right = -1, len(arr)
    while left + 1 < right:
        middle = (left + right) // 2
        if arr[middle] < elem:
            left = middle
        else:
            right = middle
    return left


def right_bound(arr, elem):
    left, right = -1, len(arr)
    while left + 1 < right:
        middle = (left + right) // 2
        if arr[middle] > elem:
            right = middle
        else:
            left = middle
    return right


def bin_search(arr, elem):
    left = left_bound(arr, elem)
    right = right_bound(arr, elem)
    return left, right
