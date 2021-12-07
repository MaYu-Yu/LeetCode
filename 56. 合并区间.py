class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        ans = []
        l, r = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= r:
                r = max(r, intervals[i][1])
            else:
                ans.append([l, r])
                l = intervals[i][0]
                r = intervals[i][1]
        ans.append([l, r])
        return ans
if __name__== "__main__":
    a = Solution()
    intervals = [[2,6],[8,10],[15,18], [1,3]]
    print(a.merge(intervals))
    intervals = [[1,4],[4,5]]
    print(a.merge(intervals))
