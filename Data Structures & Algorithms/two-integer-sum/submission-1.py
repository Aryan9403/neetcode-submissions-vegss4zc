class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_maps = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_maps:
                return [prev_maps[diff], i ]

            prev_maps[n] = i
