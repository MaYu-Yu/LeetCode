class Solution:
    def threeSum(self, nums):
        size = len(nums)
        if(not nums or size < 3):
            return []
        nums.sort()
        ans = []
        for i in range(size):
            if(nums[i] > 0):
                return ans
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            L = i+1
            R = size-1
            while(L < R):
                if(nums[i]+nums[L]+nums[R] == 0):
                    ans.append([nums[i], nums[L], nums[R]])
                    while(L < R and nums[L] == nums[L+1]):
                        L += 1
                    while(L < R and nums[R] == nums[R-1]):
                        R -= 1
                    L += 1
                    R -= 1
                elif(nums[i]+nums[L]+nums[R] > 0):
                    R -= 1
                else:
                    L = L+1
        return ans


if __name__ == '__main__':
    a = Solution()
    testList = [-1, 0, 1, 2, -1, -4]
    print(a.threeSum(testList))
