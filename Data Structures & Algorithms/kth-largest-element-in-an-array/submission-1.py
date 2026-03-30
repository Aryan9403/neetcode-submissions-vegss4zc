class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negative_nums = [-num for num in nums]
        heapq.heapify(negative_nums)
        while k>1:
            heapq.heappop(negative_nums)
            k -= 1
        res = heapq.heappop(negative_nums)
        return -(res)
