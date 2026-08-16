class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key, value, timestamp):
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.d:
            return ""

        a = self.d[key]
        l, r = 0, len(a) - 1
        ans = ""

        while l <= r:
            m = (l + r) // 2
            if a[m][0] <= timestamp:
                ans = a[m][1]
                l = m + 1
            else:
                r = m - 1

        return ans