class Solution(object):
    def insert(self, intervals, newInterval):
        ans = []
        l, r = newInterval[0], newInterval[1]
        intervals.sort()
        flag = False
        for i in intervals:
            if flag:
                ans.append([i[0], i[1]])
                continue

            if l > i[1]:
                ans.append([i[0], i[1]])
            elif r < i[0]:
                ans.append([l, r])
                ans.append([i[0], i[1]])
                flag = True
            else:    
                if r < i[1]:
                    r = i[1]
                l = min(l, i[0])
        if not flag:
            ans.append([l, r])
        return ans
if __name__== "__main__":
    a = Solution()
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(a.insert(intervals, newInterval))
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(a.insert(intervals, newInterval))
    intervals = []
    newInterval = [5,7]
    print(a.insert(intervals, newInterval))
    intervals = [[1,5]]
    newInterval = [2,3]
    print(a.insert(intervals, newInterval))