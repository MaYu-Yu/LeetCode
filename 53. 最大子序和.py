class Solution(object):
    def maxSubArray(self, nums):
        sum, ans = 0, nums[0]
        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            ans = max(ans, sum)
        return ans
if __name__== "__main__":
    a = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(a.maxSubArray(nums))
    nums = [0]
    print(a.maxSubArray(nums))
    nums = [-1]
    print(a.maxSubArray(nums))
    nums = [-100000, -1000]
    print(a.maxSubArray(nums))