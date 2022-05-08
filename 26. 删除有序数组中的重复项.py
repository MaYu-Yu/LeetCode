class Solution(object):
    def removeDuplicates(self, nums):
        l = 1
        for i in range(1, len(nums)):
            if nums[l-1] != nums[i]:
                nums[l] = nums[i]
                l+=1
        return l
if __name__== "__main__":
    a = Solution()
    print(a.removeDuplicates([1,1,2]))
    print(a.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
