def goodpairsBrute(nums):
    # returns the number of good pairs
    
    count = 0
    n = len(nums)
    
    
    for i in range(n):
        
        for j in range(i+1, n):
            
            if i < j and nums[i] == nums[j]:
                count += 1
            
     
    return count

# goodPairs using hashmap
def goodPairsHash(nums):
    
    freq = {}
    count = 0
    
    for num in nums:
        
        if num in freq:
            count += freq[num]
            freq[num] += 1
        else:
            freq[num] = 1
    
    return count
        

nums =[1, 2, 3, 1, 1, 3]

print(goodpairsBrute(nums))
print(goodPairsHash(nums))