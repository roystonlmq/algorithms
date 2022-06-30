def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        mid_pt = len(list) // 2

        if list[mid_pt] == target:
            return True
        else:
            if list[mid_pt] < target:
                return recursive_binary_search(list[mid_pt+1:], target)
            else:
                return recursive_binary_search(list[:mid_pt], target)


def verify(result):
    print('Target found: ', result)


numbers = [n for n in range(1, 9)]
result = recursive_binary_search(numbers, 6)
verify(result)

result = recursive_binary_search(numbers, 12)
verify(result)