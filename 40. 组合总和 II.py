class Solution(object):
    def combinationSum2(self, candidates, target):
        def dfs(candidates, start, end, path, ans, target):
            if target == 0: 
                ans.append(path)
                return 
            if start == end: return 
            for i in range(start, end):
                res = target - candidates[i]
                if res < 0: return 
                if start < i and candidates[i-1] == candidates[i]: continue
                dfs(candidates, i+1, end, path + [candidates[i]], ans, res)
        end = len(candidates)
        if end == 0: return [] 
        candidates.sort()
        ans = list()
        path = list()
        dfs(candidates, 0, end, path, ans, target)
        return ans 
if __name__== "__main__":
    a = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(a.combinationSum2(candidates, target))
    candidates = [2,3,5]
    target = 8
    print(a.combinationSum2(candidates, target))
    candidates = [2]
    target = 1
    print(a.combinationSum2(candidates, target))
    candidates = [2,5,2,1,2] 
    target = 5
    print(a.combinationSum2(candidates, target))
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(a.combinationSum2(candidates, target))
