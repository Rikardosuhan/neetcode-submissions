class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        maxsw = []
        temp = []

        for r in range(len(nums)):
            while temp and nums[temp[-1]] < nums[r]:
                temp.pop()

            temp.append(r)

            if temp[0] < l:
                temp.pop(0)

            if r - l + 1 == k:
                maxsw.append(nums[temp[0]])
                l += 1

        return maxsw