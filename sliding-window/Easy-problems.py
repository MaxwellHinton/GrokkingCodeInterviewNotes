# Easy sliding window problems.
# Sliding window technique can be used on linear data structures such as arrays, linked lists and strings.
# its useful when trying to find a substring, sub array, string or desired value.

# 1)

# Maximum Sum Subarray of Size K 
# given an array find the maximum sum of any contiguous subarray of size 'k'

def subArraySum(nums, k):
    
    # [2, 1, 5, 1, 3, 2]  k=3
    
    # im guessing sliding window is like we have two pointers representing the window from 1->k    
    
    n = len(nums)
    
    if n <= k:
        print("invalid")
        return -1
    
    # compute first window sum from 0 -> k
    window_sum = sum(nums[:k])
    
    max_sum = window_sum
    
    # compute sums of remaining windows by removing first element of previous window
    # and adding last element of the current window.
    
    for i in range(n-k): # n - k because last window cant exceed array.
        
        print('window sum: ', window_sum)
        window_sum = window_sum - nums[i] + nums[i + k]
        
         
    
        if window_sum > max_sum:
            max_sum = window_sum
    
    return max_sum
    
# arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
# k = 4
# print(subArraySum(arr, k))

# smallest subarray with a greater sum

# given a positive array of integers and a number 'S'. 
# find length of smallest contiguous subarray whose sum is greater than or requal to 'S'
# return length or 0

def subArrayGreaterSum(nums, s):
    
    n = len(nums)
    
    left = 0
    right = 0
    
    minimum = float('inf')
    current_sum = 0

    while right < n:
        
        # Expand the window by adding the right window value
        current_sum += nums[right]
        
        # if the sum is greater than S we need to move the entire window over again.
        while (current_sum >= s):
            minimum = min(minimum, right - left + 1)
            current_sum -= nums[left]

            left += 1
            
        right += 1
        
    return 0 if minimum == float('inf') else minimum 

nums = [2, 3, 1, 2, 4, 3]
s = 7

nums2 = [2, 1, 5, 2, 3, 2]
s2 = 7

print(subArrayGreaterSum(nums, s))
print(subArrayGreaterSum(nums2, s2))