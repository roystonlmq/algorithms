def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        mid_pt = (first + last) // 2
        if list[mid_pt] == target:
            return mid_pt
        # Number is higher, set first to be 1 integer to the right of mid_pt, last no change
        elif list[mid_pt] < target:
            first = mid_pt + 1
        # Number is lower, set last to 1 integer to the left of mid_pt, first no change
        else:
            last = mid_pt - 1

    return None