class Solution(object):
    def topKFrequent(self, nums, k):
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        arr=[]
        for i,val in count.items():
            arr.append([val,i])
        arr.sort()

        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
        