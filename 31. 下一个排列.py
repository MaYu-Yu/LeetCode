class Solution(object):
    def nextPermutation(self, nums):
        if nums == None: return
        max_size = len(nums) - 1
        R = max_size
        if R == 0: return nums
        L = R - 1
        while L >= 0:
            if nums[L] < nums[R]:
            # 找到L的下一個排序
                R = max_size
                while L < R and nums[R] <= nums[L]:
                    R-=1
                nums[L], nums[R] = nums[R], nums[L] 
                break
            else:
                R-=1
                L-=1
        # L交換完，翻轉L後面
        # 如果當前是最大排序翻轉全部
        L = L+1
        R = max_size
        while R >= L:
            nums[L], nums[R] = nums[R], nums[L]
            R-=1
            L+=1
        return nums
if __name__== "__main__":
    a = Solution()
    nums = [1,2,3]
    print(a.nextPermutation(nums))
    nums = [3,2,1]
    print(a.nextPermutation(nums))
    nums = [1,1,5]
    print(a.nextPermutation(nums))
    nums = [1]
    print(a.nextPermutation(nums))
    nums = [1,2]
    print(a.nextPermutation(nums))
    nums = [1,1]
    print(a.nextPermutation(nums))
