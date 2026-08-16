class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def backtrack(start,target,path):
            if target==0:
                ans.append(path[:])
                return 

            if target<0:
                 return 
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i,target-nums[i],path)
                path.pop()
        backtrack(0,target,[])
        return ans