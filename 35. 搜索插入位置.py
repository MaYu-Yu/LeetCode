class Solution(object):
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = ( l + r ) // 2
            if target <= nums[mid]: 
                r = mid - 1
            else: 
                l = mid + 1
        return l
if __name__== "__main__":
    a = Solution()
    nums, target = [5,7,8,10], 8
    print(a.searchInsert(nums, target))
    nums, target = [5,7,8,10], 6
    print(a.searchInsert(nums, target))
    nums, target = [7,8], 8
    print(a.searchInsert(nums, target))
    nums, target = [1], 0
    print(a.searchInsert(nums, target))
    nums, target = [2,2], 2
    print(a.searchInsert(nums, target))
    nums, target = [1], 1
    print(a.searchInsert(nums, target))
    nums, target = [1,2,3], 1
    print(a.searchInsert(nums, target))
    nums, target = [1,3], 3
    print(a.searchInsert(nums, target))
    nums, target = [1,3,5], 3
    print(a.searchInsert(nums, target))