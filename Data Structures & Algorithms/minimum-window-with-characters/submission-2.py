class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count = {}

        for ch in t:
            count[ch] = count.get(ch, 0) + 1

        window = {}
        l = 0
        have = 0
        need = len(count)

        ans = ""
        ansLen = float("inf")

        for r in range(len(s)):

            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            if ch in count and window[ch] == count[ch]:
                have += 1

            while have == need:

                if r - l + 1 < ansLen:
                    ans = s[l:r+1]
                    ansLen = r - l + 1

                left = s[l]
                window[left] -= 1

                if left in count and window[left] < count[left]:
                    have -= 1

                l += 1

        return ans