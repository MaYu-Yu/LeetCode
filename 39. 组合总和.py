class Solution(object):
    def combinationSum(self, candidates, target):
        def dfs(candidates, start, end, path, ans, target):
            if target == 0: 
                ans.append(path)
                return 

            for i in range(start, end):
                res = target - candidates[i]
                if res < 0: break
                dfs(candidates, i, end, path+[candidates[i]], ans, res)

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
    print(a.combinationSum(candidates, target))
    candidates = [2,3,5]
    target = 8
    print(a.combinationSum(candidates, target))
    candidates = [2]
    target = 1
    print(a.combinationSum(candidates, target))
    candidates = [1] 
    target = 1
    print(a.combinationSum(candidates, target))
    candidates = [1]
    target = 2
    print(a.combinationSum(candidates, target))
