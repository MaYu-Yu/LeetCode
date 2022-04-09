    # :type nums: List[int]
    # :type limit: int
    # :rtype: int
class Solution:
    def longestSubarray(self, nums, limit):
        from sortedcontainers import SortedList
        slist = SortedList() 

        nums_len = len(nums)
        left = right = result =  0

        while right < nums_len:
            slist.add(nums[right])
            while slist[-1] - slist[0] > limit:
                slist.remove(nums[left])
                left+=1
            result = max(result, right - left + 1)
            right+=1
        return result

if __name__ == "__main__":
    a = Solution()
    print(a.longestSubarray([1,5,6,7,8,10,6,5,6],4))