class Solution:
    def maxArea(self, height) -> int:
        size = len(height)
        left = ans =  0
        right = size-1
        while left != right:
            area = ( right - left ) * min(height[left], height[right])
            ans =  max(ans, area)
            if height[left] < height[right]: left+=1
            else: right-=1
        return ans


if __name__ == '__main__':
    a = Solution()
    testList = [1,8,6,2,5,4,8,3,7]
    print(a.maxArea(testList))
