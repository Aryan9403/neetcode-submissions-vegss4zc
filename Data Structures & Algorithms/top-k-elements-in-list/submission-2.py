class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}

        for num in nums:
            frequent[num] = frequent.get(num,0) + 1
        
        arr = []
        for i, cnt in frequent.items():
            arr.append([cnt, i])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
