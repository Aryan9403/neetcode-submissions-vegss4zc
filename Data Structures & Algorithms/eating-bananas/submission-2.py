class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0
        
        l, r = 1, max(piles)
        res = r
        while l<=r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours<=h:
                res = min(k, r)
                r = k - 1
            else: 
                l = k+1
        return res