class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        subset = []
        res = []
        candidates.sort()
        
        def dfs(start):

            if sum(subset)==target:
                res.append(subset.copy())
                return 
            
            elif sum(subset)>target:
                return

            elif start>=len(candidates):
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                subset.append(candidates[i])
                dfs(i+1)
                subset.pop()


        dfs(0)
        return res