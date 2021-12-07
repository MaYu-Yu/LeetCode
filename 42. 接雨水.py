from debug import debug_class
DEBUG = debug_class(True)
class Solution(object):
    def trap(self, height):
        size = len(height)
        if size < 3: return 0
        l, r = 0, size - 1
        l_max, r_max = height[l], height[r]
        rain_water = 0
        while(l < r):
            if l_max <= r_max:
                l+=1
                if l_max <= height[l]:
                    l_max = height[l] 
                else:
                    rain_water += l_max - height[l]
                
            else:
                r-=1
                if height[r] >= r_max:
                    r_max = height[r] 
                else:
                    rain_water += r_max - height[r]
        return rain_water
if __name__== "__main__":
    a = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(a.trap(height))
    height = [4,2,0,3,2,5]
    print(a.trap(height))    
    height = [4,2,3]
    print(a.trap(height))        
    height = [5,5,1,7,1,1,5,2,7,6]
    print(a.trap(height)) 