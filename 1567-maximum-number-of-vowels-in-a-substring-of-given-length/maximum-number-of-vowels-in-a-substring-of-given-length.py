class Solution(object):
    def maxVowels(self, s, k):
        vowels = set('aeiou')
        
        # Step 1: count vowels in first window
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        
        max_vowels = count
        
        # Step 2: sliding window
        for i in range(k, len(s)):
            # add new character
            if s[i] in vowels:
                count += 1
            
            # remove old character
            if s[i - k] in vowels:
                count -= 1
            
            # update max
            max_vowels = max(max_vowels, count)
        
        return max_vowels