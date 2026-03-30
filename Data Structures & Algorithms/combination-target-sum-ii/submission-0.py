class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, cur):
        #Base Case            
            #check for seeing if index i is less
            
            if i == len(candidates):
                if sum(cur) == target:
                    res.append(cur.copy())
                return

            if sum(cur) == target:
                res.append(cur.copy())
                return
            
                    
            cur.append(candidates[i])
                
            backtrack(i+1, cur)
            cur.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, cur)

        backtrack(0, [])
        return res
        