class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1 

        return len(set(freq.values())) == 1  #{2}