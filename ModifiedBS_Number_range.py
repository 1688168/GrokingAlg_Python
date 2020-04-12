def find_range(arr, key):
    result = [- 1, -1]
    # find max
    ll = bs(arr, key, True)
    if ll < 0 or ll >= len(arr):
        return result
    # find min
    rr = bs(arr, key, False)
    # return range
    result[0], result[1] = ll, rr
    return result


def bs(arr, key, is_min):
    left = 0
    right = len(arr) - 1
    min_idx = len(arr)
    if not is_min:
        min_idx = 0

    while left <= right:
        mid = left + (right - left) // 2

        #print("ll: {left}, rr: {right}, mid: {mid}".format(left=left, right=right, mid=mid))

        if arr[mid] > key:
            right = mid - 1
        elif arr[mid] == key:
            min_idx = min(mid, min_idx) if is_min else max(mid, min_idx)
            if is_min:
                right = mid - 1
            else:
                left = mid + 1
        else:
            left = mid + 1

    return min_idx


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))

main()