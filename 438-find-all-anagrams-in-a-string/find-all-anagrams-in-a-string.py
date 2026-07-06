class Solution(object):
    def findAnagrams(self, s, p):
        from collections import Counter
        
        result = []
        p_count = Counter(p)
        window_count = Counter()
        
        k = len(p)
        
        for i in range(len(s)):
            # Add current character
            window_count[s[i]] += 1
            
            # Remove left character if window > k
            if i >= k:
                if window_count[s[i - k]] == 1:
                    del window_count[s[i - k]]
                else:
                    window_count[s[i - k]] -= 1
            
            # Compare window with pattern
            if window_count == p_count:
                result.append(i - k + 1)
        
        return result ###👉 p_count = {a:1, b:1, c:1}
#👉 k = 3 (window size)
#🔄 Iteration Table (Step by Step)
#👉 i = 0
#Add 'c'
#window = {c:1}
#size < 3 → no removal
#❌ Not match
'''👉 i = 1
Add 'b'
window = {c:1, b:1}
size < 3
❌ Not match
👉 i = 2
Add 'a'
window = {c:1, b:1, a:1}
size = 3 ✅
Compare with {a:1,b:1,c:1} → ✅ MATCH
👉 Add index:
i - k + 1 = 2 - 3 + 1 = 0
✔ result = [0]
👉 i = 3
Add 'e'
window = {c:1, b:1, a:1, e:1}
Now size > 3 → remove left (i-k = 0 → 'c')
Remove 'c'
window = {b:1, a:1, e:1}
❌ Not match
👉 i = 4
Add 'b'
window = {b:2, a:1, e:1}
Remove left (i-k = 1 → 'b')
window = {b:1, a:1, e:1}
❌ Not match
👉 i = 5
Add 'a'
window = {b:1, a:2, e:1}
Remove left (i-k = 2 → 'a')
window = {b:1, a:1, e:1}
❌ Not match
👉 i = 6
Add 'b'
window = {b:2, a:1, e:1}
Remove left (i-k = 3 → 'e')
window = {b:2, a:1}
❌ Not match
👉 i = 7
Add 'a'
window = {b:2, a:2}
Remove left (i-k = 4 → 'b')
window = {b:1, a:2}
❌ Not match
👉 i = 8
Add 'c'
window = {b:1, a:2, c:1}
Remove left (i-k = 5 → 'a')
window = {b:1, a:1, c:1}
✅ MATCH
👉 index:
8 - 3 + 1 = 6
✔ result = [0, 6]
👉 i = 9
Add 'd'
window = {b:1, a:1, c:1, d:1}
Remove left (i-k = 6 → 'b')
window = {a:1, c:1, d:1}'''
#❌ Not match