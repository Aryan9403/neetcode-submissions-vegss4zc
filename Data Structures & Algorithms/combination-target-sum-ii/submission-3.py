class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        subset = []
        res = []
        candidates.sort()
        
        def dfs(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return 

            elif sum(subset)>target:
                return

            elif i>=len(candidates):
                return

            for start in range(i, len(candidates)):
                if start>i and candidates[start]==candidates[start-1]:
                    continue

                subset.append(candidates[start])
                dfs(start+1)
                subset.pop()
            
        dfs(0)
        return res