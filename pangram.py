def isPangram(str):
    
    seen = set()
    
    str = str.lower()
    
    
    for s in str:
        print(s)
        if s.isalpha():
            seen.add(s)
        
    print(len(seen))
    
    return len(seen) == 26

sentence = "TheQuickBrownFoxJumpsOverTheLazyDog"

print(isPangram(sentence))    