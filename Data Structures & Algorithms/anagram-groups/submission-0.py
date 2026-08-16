class Solution:
    def groupAnagrams(self, strs):
        m=defaultdict(list)
        for i in strs:
            sorteds=''.join(sorted(i))
            m[sorteds].append(i)
        return list(m.values())
