mod=(10**9+7)

class Solution:
    def topDown(self, n):
        # Code here
        def solver(n,memo={}):
            if(n<=1):
                return n
            elif(n in memo):
                return memo[n]
                
            memo[n]=(solver(n-1,memo)+solver(n-2,memo))%mod
            
            return memo[n]
        
        return solver(n)
        
    def bottomUp(self, n):
        # Code here
        if(n<=1):
            return n
            
        prev1,prev2=0,1
        
        for i in range(2,n+1):
            current=(prev1+prev2)%mod
            prev1=prev2
            prev2=current
        
        return prev2
