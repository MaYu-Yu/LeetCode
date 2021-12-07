class Solution:
    def countAndSay(self, n):
        if n == 1:
            return '1'
        ans = '1'
        for _ in range(n - 1):
            temp = '1'
            ans_t = ''
            times = 0
            for i in ans:
                if i != temp: 
                    if times != 0:
                        ans_t += str(times) + temp 
                    temp = i
                    times = 1
                else:
                    times+=1
            ans = ans_t + str(times) + temp 
        return ans
if __name__== "__main__":
    a = Solution()
    for nums in range(1, 10):
        print(nums, '[',a.countAndSay(nums), ']')

