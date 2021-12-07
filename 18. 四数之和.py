class Solution:
    def fourSum(self, nums, target):
        ans = []
        if not nums or len(nums) < 4:
            return ans
        
        nums.sort()
        size = len(nums)
        for i in range(size - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[size - 3] + nums[size - 2] + nums[size - 1] < target:
                continue
            for j in range(i + 1, size - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[size - 2] + nums[size - 1] < target:
                    continue
                L, R = j + 1, size - 1
                while L < R:
                    sum = nums[i] + nums[j] + nums[L] + nums[R]
                    if sum == target:
                        ans.append([nums[i], nums[j], nums[L], nums[R]])
                        while L < R and nums[L] == nums[L + 1]:
                            L += 1
                        L += 1
                        while L < R and nums[R] == nums[R - 1]:
                            R -= 1
                        R -= 1
                    elif sum < target:
                        L += 1
                    else:
                        R -= 1
        return ans
if __name__ == '__main__':
    a = Solution()
    nums = [1,0,-1,0,-2,2]
    target = 0
    print(a.fourSum(nums, target))
    print(a.fourSum([], 0))
