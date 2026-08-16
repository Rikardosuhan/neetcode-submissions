class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count={}
        for ch in t:
            count[ch]=1+count.get(ch,0)
        l=0
        window={}
        need=len(count)
        ans=""
        anslen=float("inf")
        have=0
        for r in range(len(s)):
            ch=s[r]
            window[ch]=1+window.get(ch,0)
            if ch in count and window[ch]==count[ch]:
                have+=1
            while have==need:
                if r-l+1 < anslen:
                    ans=s[l:r+1]
                    anslen=r-l+1
                left=s[l]
                window[left]-=1
                if left in count and window[left]<count[left]:
                    have-=1
                l+=1
        return ans

