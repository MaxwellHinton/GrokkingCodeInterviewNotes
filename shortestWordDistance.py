def shortestWordDistance(words, word1, word2):
    
    index1 = -1
    index2 = -1
    
    distance = float('inf')
    
    # traverse through the list 
    for i, word in enumerate(words):
        
        # if we encounter either word, set the respective index to the i
        if word == word1:
            index1 = i
        elif word == word2:
            index2 = i
            
        # check if both words have been found. Subtract index's to find distance.
        if index1 != -1 and index2 != -1:
            distance = min(distance, abs(index1 - index2))
        
    return distance

words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "practice"
word2 = "coding"

print(shortestWordDistance(words, word1, word2))
    
            
            
    