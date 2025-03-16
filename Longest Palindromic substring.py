class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n= len(s)
        if n==0: 
            return ""
        dp= [[False]*n for _ in range(n)]
        start, maxlength= 0, 1
        for i in range(n): 
            dp[i][i]=True
        for i in range(n-1): 
            if s[i]==s[i+1]: 
                dp[i][i+1]=True
                start, maxlength= i, 2
        for length in range(3, n+1): 
            for i in range(n-length+1): 
                j= i+ length -1
                if s[i]==s[j] and dp[i+1][j-1]==True: 
                    dp[i][j]=True
                    start, maxlength= i, length
        return s[start: start+maxlength]