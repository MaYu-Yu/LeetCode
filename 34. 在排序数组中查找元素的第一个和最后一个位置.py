class Solution(object):
    def searchRange(self, nums, target):
        if not nums: return [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = ( l + r ) // 2
            if nums[mid] == target:
                l = r = mid
                while 0 < l and target == nums[l - 1]: l-=1
                while r < len(nums) - 1 and target == nums[r + 1]: r+=1
                break
            if target < nums[mid]: r = mid - 1
            else: l = mid + 1
        return [-1, -1] if l > r else [l, r]
if __name__== "__main__":
    a = Solution()
    nums, target = [5,7,7,8,8,10], 8
    print(a.searchRange(nums, target))
    nums, target = [5,7,7,8,8,10], 6
    print(a.searchRange(nums, target))
    nums, target = [7,7,8], 8
    print(a.searchRange(nums, target))
    nums, target = [1], 0
    print(a.searchRange(nums, target))
    nums, target = [2,2], 2
    print(a.searchRange(nums, target))
    nums, target = [1], 1
    print(a.searchRange(nums, target))
    nums, target = [1,2,3], 1
    print(a.searchRange(nums, target))