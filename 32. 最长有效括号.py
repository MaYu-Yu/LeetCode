class Solution:
    def longestValidParentheses(self, s) :
        stack = [-1]
        max_lens = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack: stack.append(i) #起始點紀錄
                else: 
                    max_lens = max(max_lens, i - stack[-1])
        return max_lens
if __name__== "__main__":
    a = Solution()
    arr = ["(()",
    ")()())",
    "()(()",
    "()()()((()))",
    ")(",
    ")()())()()(",
    "(()))())(",
    "(())(",
    "(()(((()",
    ""]
    for nums in arr:
        print(a.longestValidParentheses(nums))

