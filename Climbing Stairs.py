class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2: 
            return n
        F= [0]* (n+1)
        F[1]=1
        F[2]=2
        for i in range(3,n+1): 
            F[i]= F[i-1]+F[i-2]
        return F[n]
        