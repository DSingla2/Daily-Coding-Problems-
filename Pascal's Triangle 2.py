class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp= [[1]*(i+1) for i in range(rowIndex+1)]
        if rowIndex==0 or rowIndex==1: 
            return dp[rowIndex]
        for i in range(2,rowIndex+1):
            for j in range(1,i):
                dp[i][j]= dp[i-1][j-1]+dp[i-1][j]
        return dp[rowIndex]
