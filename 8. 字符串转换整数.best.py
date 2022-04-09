class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        minus_flag = False # minus or not
        load_flag = False
    #清理空格
        s = s.strip()
        for word in s:
        # if loading -> just numbers
            if load_flag: 
                if ord(word) > 57 or ord(word) < 48: break
                ans = ans*10 + int(word)
                if minus_flag:
                    if ans > -boundry: return boundry
                else: 
                    if ans > boundry: return boundry
                continue
            else:
            # numbers
                if ord(word) < 58 and ord(word) > 47:
                    load_flag = True 
                    ans = int(word)
                elif ord(word) == 45: minus_flag = load_flag = True # minus
                elif ord(word) == 43: load_flag = True # plus
                else: return 0 #如果起始不是上面那些則return 0
            # overflow
                boundry = -(1<<31) if minus_flag else (1<<31) -1   
        return -ans if minus_flag else ans
if __name__ == '__main__':
    a = Solution()
    print(a.myAtoi("4193 with words"))