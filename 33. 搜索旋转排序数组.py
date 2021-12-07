class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            if nums[0] <= nums[mid]: # 左方正常排序
                if nums[0] <= target < nums[mid]: 
                    r = mid - 1
                else: l = mid + 1
            else: # 右方正常排序
                if nums[mid] < target <= nums[-1]: l = mid + 1
                else: r = mid - 1
        return -1
if __name__== "__main__":
    a = Solution()
    nums, target = [4,5,6,7,0,1,2], 0
    print(a.search(nums, target))
    nums, target = [4,5,6,7,0,1,2], 3
    print(a.search(nums, target))
    nums, target = [1,3], 3
    print(a.search(nums, target))
    nums, target = [5,1,3], 3
    print(a.search(nums, target))
        