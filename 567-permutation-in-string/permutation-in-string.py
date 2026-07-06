from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        if n > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:n])

        if s1_count == window_count:
            return True

        for i in range(n, len(s2)):
            # Add new character
            window_count[s2[i]] += 1

            # Remove leftmost character
            left_char = s2[i - n]
            window_count[left_char] -= 1

            # Remove key if its count becomes 0
            if window_count[left_char] == 0:
                del window_count[left_char]

            if window_count == s1_count:
                return True

        return False