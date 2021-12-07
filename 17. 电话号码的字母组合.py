class Solution:
    def letterCombinations(self, digits: str):
        if not digits: return []

        char_list = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        queue = [''] 

        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for c in char_list[ord(digit)-50]:
                    queue.append(tmp + c)
        return queue


if __name__ == '__main__':
    a = Solution()
    print(a.letterCombinations("23"))
    print(a.letterCombinations(""))
    print(a.letterCombinations("2"))
