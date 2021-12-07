class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        if size == 1: return 1
        result = 0
        for left in range(size):
            alist = []
            alist.append(s[left])
            max_len = 1
            for right in range(left+1, size): 
                if s[right] in alist: break
                alist.append(s[right])
                max_len +=1
            if max_len > result: result = max_len 
        return result 
        

if __name__ == '__main__':
    a = Solution()
    word = "abcabcbb"    
    print(a.lengthOfLongestSubstring(word))