class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums: 
            count[num] = count.get(num,0) + 1

        count2 = []
        for num,count in count.items():
            count2.append([count, num])
        count2.sort()

        res = []
        while len(res)<k:
            res.append(count2.pop()[1])
        return res