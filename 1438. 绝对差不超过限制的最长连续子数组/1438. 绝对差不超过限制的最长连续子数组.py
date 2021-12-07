    # :type nums: List[int]
    # :type limit: int
    # :rtype: int
class Solution:
    def longestSubarray(self, nums, limit):
        result_len = 0
    #一個值完成所有的絕對差則刪除其
        for i in range(len(nums)):
            nums0 = nums[i:] #nums
        #製造連續數列
            for j in range(len(nums0)):
                list0 = nums0[:j+1]
            #取最大絕對差          
                list0_abs = abs(max(list0) - min(list0))
            #任兩個值的abs不可超過limit
                if list0_abs > limit: break
                elif result_len < len(list0): result_len = len(list0)
            #看此次連續數列是否有大於others，更新result長度
        return result_len
        
if __name__ == "__main__":
    a = Solution()
    print(a.longestSubarray([1,5,6,7,8,10,6,5,6],4))