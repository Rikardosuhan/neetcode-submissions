class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setnums=set(nums)
        
        if(len(nums)!=len(setnums)):
            return True
        else:
            return False