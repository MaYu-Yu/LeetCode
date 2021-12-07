class Solution(object):
    def removeDuplicates(self, nums):
        temp = None
        used = 0
        for i in range(len(nums)):
            if nums[i] != temp:
                temp = nums[i]
                nums[used] = temp
                used+=1
        return used
if __name__== "__main__":
    a = Solution()
    print(a.removeDuplicates([1,1,2]))
    print(a.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
