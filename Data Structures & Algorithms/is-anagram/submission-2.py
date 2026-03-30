class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        set_s = {}
        set_t = {}
        
        for ch in s:
            set_s[ch] = set_s.get(ch, 0) + 1

        for ch in t:
            set_t[ch] = set_t.get(ch, 0) + 1

        return set_s == set_t
        