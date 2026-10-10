class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        subset = []
        res = []
                 
            
        def dfs(i):

            if sum(subset)==target:
                res.append(subset.copy())
                return
            
            elif sum(subset)>target:
                return

            if i>=len(nums):
                return
            
            subset.append(nums[i])
            dfs(i)
            subset.pop()
            dfs(i+1)


        dfs(0)
        return res