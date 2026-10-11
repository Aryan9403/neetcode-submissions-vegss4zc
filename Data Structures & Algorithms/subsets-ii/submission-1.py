class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        subset=[]
        res=[]
        nums.sort()

        def dfs(i):
            
            res.append(subset.copy())

            for start in range(i, len(nums)):
                if start>i and nums[start] == nums[start-1]:
                    continue

                subset.append(nums[start])
                dfs(start+1)
                subset.pop()
            
        dfs(0)
        return res