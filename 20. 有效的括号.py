class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False #基數88
        other = { ")": "(",
            "]": "[",
            "}": "{" 
        }
        stack = []
        for i in s:
            if i in other: 
                if stack == [] or stack[-1] != other[i]: return False
                stack.pop()
            else:
                stack.append(i)
        return True if len(stack) == 0 else False
if __name__ == '__main__':
    a = Solution()
    s = "()"
    s0 = "()[]{}"
    s1 = "(]"
    print(a.isValid(s))
    print(a.isValid(s0))
    print(a.isValid(s1))