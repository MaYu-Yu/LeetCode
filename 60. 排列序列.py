class Solution:
    def getPermutation(self, n, k):
        def dfs(used, n, k, index, path):
            if index == n:
                return
            cnt = factorial[n - 1 - index]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cnt < k:
                    k -= cnt
                    continue
                path.append(i)
                used[i] = True
                dfs(used, n, k, index + 1, path)
                return
        if n == 0:
            return ""

        used = [False for _ in range(n + 1)]
        path = []
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i
        dfs(used, n, k, 0, path)
        return ''.join([str(num) for num in path])
if __name__== "__main__":
    a = Solution()
    n = 3
    k = 3
    print(a.getPermutation(n,k))
    n = 4 
    k = 9
    print(a.getPermutation(n,k))
    n = 3 
    k = 1
    print(a.getPermutation(n,k))