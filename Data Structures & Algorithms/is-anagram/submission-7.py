class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}
        for ch in s:
            hashmap_s[ch] = hashmap_s.get(ch, 0) + 1

        for ch in t:
            hashmap_t[ch] = hashmap_t.get(ch, 0) + 1

        if hashmap_s == hashmap_t:
            return True
        return False