class Solution(object):
    def firstMissingPositive(self, nums):
        size = len(nums)
    # -不討論
        for i in range(size):
            if nums[i] <= 0:
                nums[i] = size + 1
    # 哈希轉換
        for i in range(size):
            num = abs(nums[i])
            if num <= size:
                nums[num - 1] = -abs(nums[num - 1] )
    #搜尋
        for i in range(size):
            if nums[i] > 0:
                return i + 1
        return size + 1
if __name__== "__main__":
    a = Solution()
    nums = [1,2,0]
    print(a.firstMissingPositive(nums))
    nums = [3,4,-1,1]
    print(a.firstMissingPositive(nums))
    nums = [7,8,9,11,12]
    print(a.firstMissingPositive(nums))
    nums = [1,2,6,3,5,4]
    print(a.firstMissingPositive(nums))