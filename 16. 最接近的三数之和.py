class Solution:
    def threeSumClosest(self, nums, target) -> int:
        size = len(nums)
        if(not nums or size < 3):
            return 0
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(size):
            left, right = i+1, size-1
            while left < right:
                Sum = nums[i] + nums[left] + nums[right]
                if Sum == target:
                    return target
                elif Sum < target:
                    left += 1
                else:
                    right -= 1
                if abs(target - Sum) <= abs(target - ans):
                    ans = Sum
        return ans


if __name__ == '__main__':
    a = Solution()
    testList = [1,2,5,10,11]
    target = 12
    print(a.threeSumClosest(testList, target))
