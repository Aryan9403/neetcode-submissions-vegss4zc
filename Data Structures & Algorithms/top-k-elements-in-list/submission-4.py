class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        array = []
        for num, cnt in seen.items():
            array.append([cnt, num])

        array.sort()
        
        result = []
        while len(result) < k:
            result.append(array.pop()[1])

        return result