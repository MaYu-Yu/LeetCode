class Solution(object):
    def canJump(self, nums):
        size = len(nums)
        max_step = 0
        end = nums[0]
        for i in range(size):
            max_step = max(max_step, i + nums[i])
            if i == end:
                if end == max_step and end < size - 1: 
                    return False
                end = max_step
        return True        
                

if __name__== "__main__":
    a = Solution()
    nums = [2,3,1,1,4]
    print(a.canJump(nums))
    nums = [3,2,1,0,4]
    print(a.canJump(nums))
    nums = [0]
    print(a.canJump(nums))   
