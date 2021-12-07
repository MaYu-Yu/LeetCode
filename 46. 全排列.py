from debug import debug_class
DEBUG = debug_class(True)
class Solution:
    def permute(self, nums):
        def backtrack(nums, size, ans, head):
            if head == size:
                ans.append(nums[:])
            for i in range(head, size):
                nums[head], nums[i] = nums[i], nums[head]
                backtrack(nums, size, ans, head + 1)
                nums[head], nums[i] = nums[i], nums[head]

        size = len(nums)
        ans = []
        backtrack(nums, size, ans, 0)
        return ans
if __name__== "__main__":
    a = Solution()
    nums = [1,2,3,4]
    print(a.permute(nums))
    nums = [1,2,3]
    print(a.permute(nums))
    nums = [0,1]
    print(a.permute(nums))
    nums = [1]
    print(a.permute(nums))