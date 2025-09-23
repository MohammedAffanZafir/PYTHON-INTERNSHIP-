def first_occurrence(arr, key):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            result = mid
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return result


def last_occurrence(arr, key):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            result = mid
            low = mid + 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return result
# Example usage
nums = [1, 2, 4, 4, 4, 5, 6, 7]
key = 4

first = first_occurrence(nums, key)
last = last_occurrence(nums, key)

if first != -1:
    print(f"First occurrence of {key}: Index {first}")
    print(f"Last occurrence of {key}: Index {last}")
else:
    print(f"{key} not foundinthelist")