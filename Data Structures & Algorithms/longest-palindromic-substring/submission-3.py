class Solution:
    def longestPalindrome(self, s: str) -> str:
        #okay so the sub problem here seems to be that we find a palindrom compare with the previous found palindrome and if the curr is longer we update
        #how to find a palindrome? 
        res = ""
        resLen = 0

        for i in range(len(s)):
            #odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res=s[l:r+1]
                    resLen =r-l+1

                l-=1
                r+=1
                


            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1)>resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1

        return res



