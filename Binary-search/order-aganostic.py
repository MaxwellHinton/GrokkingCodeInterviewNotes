# sorted array of numbers, find if a given number 'key' is present. 
# unaware if array is sorted in ascending or descending order.

# returns index of key or -1

def orderAgnostic(nums, key):
    
    n = len(nums)
    
    # base case
    if n == 0:
        return -1

    is_ascending = nums[0] < nums[n - 1]
    
    return binary_search(nums, key, 0, n - 1, is_ascending)

def binary_search(arr, key, start, end, is_ascending):
    if start > end:
        return - 1
    
    mid = (start + end) // 2
    print("Array: ", arr[start:end+1])
    print("Mid index: ", mid, "Mid value: ", arr[mid])
    
    if arr[mid] == key:
        return mid
    elif is_ascending:
        if arr[mid] < key:
            return binary_search(arr, key, mid + 1, end, is_ascending)
        else:
            return binary_search(arr, key, start, mid - 1, is_ascending)
    else: # descending order
        if arr[mid] < key:
            return binary_search(arr, key, start, mid - 1, is_ascending)
        else:
            return binary_search(arr, key, mid + 1, end, is_ascending)
    

nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
key = 72
print(orderAgnostic(nums, key))