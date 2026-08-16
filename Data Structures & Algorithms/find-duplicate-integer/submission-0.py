class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count={}
        res=0
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for val in count.keys():
            if count[val]>1:
                res=val
        
        return res
