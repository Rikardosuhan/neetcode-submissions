class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        if target not in nums:
            return -1
        else:
            while l<=r:
                if nums[l]==target:
                    return l
                else:
                    l+=1