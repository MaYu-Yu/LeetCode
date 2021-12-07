from debug import debug_class
DEBUG = debug_class(True)
class Solution(object):
    def permuteUnique(self, nums):
        def backtrack(nums, ans, head, size, used, temp):
            if head == size:
                ans.append(temp)
                return
            for i in range(size):
                if not used[i]:
                    if i > 0 and not used[i - 1] and nums[i] == nums[i - 1]:
                        continue
                    used[i] = True
                    backtrack(nums, ans, head + 1, size, used, temp+[nums[i]])
                    used[i] = False
        ans = []
        nums.sort()
        used = [False for _ in range(len(nums))]
        backtrack(nums, ans, 0, len(nums), used, [])
        return ans
if __name__== "__main__":
    a = Solution()
    nums = [1,1,2]
    print(a.permuteUnique(nums))
    nums = [0,1,0,0,9]
    print(a.permuteUnique(nums))    
    nums = [1,2,3]
    print(a.permuteUnique(nums))