class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setA = set()
        for num in nums:
            if num in setA:
                return True
            setA.add(num)
        return False
