class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        #(n-2) instead of (n-1) because if there are 3 numbers 1,2,3 we still have 2 numbers for 2 pointers instead of left with no number of the 2nd pointer
        for i in range(n-2):
            if i>0 and nums[i-1]==nums[i]:
                continue


            l = i+1
            r = n-1

            while l<r:
                s = nums[i] + nums[l] + nums[r] 

                if s==0:
                    res.append([nums[i], nums[l], nums[r]])

                    l+=1
                    r-=1

                    while l<r and nums[l] == nums[l-1]:
                        l+=1

                    while l<r and nums[r] == nums[r+1]:
                        r-=1

                elif s<0:
                    l+=1

                elif s>0:
                    r-=1

        return res








             
        