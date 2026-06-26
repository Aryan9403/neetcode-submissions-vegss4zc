class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_t = {}
        seen_s = {}

        for ch in s:
            seen_s[ch] = seen_s.get(ch, 0) + 1

        for ch in t:
            seen_t[ch] = seen_t.get(ch, 0) + 1

        if seen_t == seen_s:
            return True
        return False