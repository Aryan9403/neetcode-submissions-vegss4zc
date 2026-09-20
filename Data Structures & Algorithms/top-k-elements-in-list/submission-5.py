class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1 
        array = []
        while k>0:
            max_key = max(hashmap, key=hashmap.get)
            array.append(max_key)
            hashmap.pop(max_key)
            k-=1
        return array


