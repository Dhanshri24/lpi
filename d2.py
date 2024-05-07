def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return -1

# Example usage:
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
