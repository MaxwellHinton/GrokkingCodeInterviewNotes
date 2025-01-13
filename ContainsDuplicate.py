def containsDuplicatesHash(nums):
    
    # two ways:
        # we can brute force by iterating over the list with complexity O(N^2)
        
        # use hashmap to store seen values - still O(N) complexity
    
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False    


def containsDuplicatesBrute(nums):
    
    for i in range(len(nums)):
        
        for j in range(i+1, len(nums)):
            
            if nums[i] == nums[j]:
                return True
            
    return False

def containsDuplicateSorted(nums):
    
    nums.sort()
    
    for i in range(len(nums) - 1, 0, -1):
        print(i)
        if nums[i] == nums[i - 1]:
            return True

    return False 

nums = [1, 2, 3, 1, 4, 5, 6]
print("Hash set: ", containsDuplicatesHash(nums))
print("Brute force: ", containsDuplicatesBrute(nums))
print("Sorting: ", containsDuplicateSorted(nums))
        