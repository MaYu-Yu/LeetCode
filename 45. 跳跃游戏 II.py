from debug import debug_class
DEBUG = debug_class(True)
class Solution:
    def jump(self, nums):
        Max_step, end, step = 0, 0, 0
        for i in range(len(nums) - 1):
            if Max_step >= i:
                Max_step = max(Max_step, i + nums[i])
                if i == end:
                    end = Max_step
                    step += 1
        return step
if __name__== "__main__":
    a = Solution()
    nums = [2,3,1,1,4]
    print(a.jump(nums))
    nums = [1,7,0,1,4]
    print(a.jump(nums))
    nums = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
    print(a.jump(nums))