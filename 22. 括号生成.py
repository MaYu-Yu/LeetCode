class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        def backtrack(temp, left, right):
            if len(temp) == 2 * n:
                # print("[join]", temp)
                ans.append(''.join(temp))
                return
            if left < n:
                temp.append('(')
                # print("[left do (", temp)
                backtrack(temp, left+1, right)
                temp.pop()
                # print("[left do pop ]", temp)
            if right < left:
                temp.append(')')
                # print("[left do )", temp)
                backtrack(temp, left, right+1)
                temp.pop()
                # print("[right do pop ]", temp)

        backtrack([], 0, 0)
        return ans           
                    
if __name__ == '__main__':
    a = Solution()
    n = 3
    print(a.generateParenthesis(n))