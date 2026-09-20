class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            array = [0]*26
            for ch in s:
                array[ord(ch) - ord('a')] += 1
            hashmap[tuple(array)].append(s)
        return list(hashmap.values())