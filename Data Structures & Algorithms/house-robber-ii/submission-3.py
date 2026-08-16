class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return  nums[0]
        def solve(a):
            m=len(a)
            dp=[0]*m
            if m==1:
                return a[0]
            dp[0]=a[0]
            dp[1]=max(a[0],a[1])
            for i in range(2,m):
                dp[i]=max(dp[i-1],dp[i-2]+a[i])
            return dp[m-1]
        return max(solve(nums[:-1]),solve(nums[1:]))
        
        