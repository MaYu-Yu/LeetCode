class Solution(object):
    def sortColors(self, nums):
        i, l, r = 0, 0, len(nums) - 1
        while(i <= r):
            if nums[i] == 2 and i < r:
                while nums[r] == 2 and i < r: r-=1 # 如果nums[r]已經是2了，r界線往前一項
                nums[i], nums[r] = nums[r], nums[i]
                r-=1
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l+=1
            i+=1
        return nums
if __name__ == "__main__":
    a = Solution()
    nums = [1,2,2]
    print(a.sortColors(nums))    
    nums = [1,2,0]
    print(a.sortColors(nums))
    nums = [1,2]
    print(a.sortColors(nums))