class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        from sortedcontainers import SortedList
        alist = SortedList()
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 != 0: alist.update(nums1)    
        if len2 != 0: alist.update(nums2)
        lena = len1+len2
        if lena == 0:
            return 0.0
        elif lena == 1: 
            return float(alist[0])
        elif lena == 2:
            return (alist[0] + alist[1]) /2.0
    #奇偶數
        elif lena % 2 != 0:   
            return float(alist[lena//2])
        else:
            return (alist[lena//2] + alist[lena//2-1]) /2.0
        return alist
if __name__ == '__main__':    
    a = Solution()
    print(a.findMedianSortedArrays([1,3],[2]))