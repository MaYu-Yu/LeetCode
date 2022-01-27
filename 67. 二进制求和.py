class Solution(object):
    def addBinary(self, a, b):
        ans = ""
        ai = len(a) - 1
        bi = len(b) - 1
        tc = 0
        while ai >= 0 or bi >= 0:
            ta, tb = 0, 0
            if ai >= 0: 
                ta = int(a[ai])
                ai -= 1
            if bi >= 0:
                tb = int(b[bi])
                bi -= 1
            ans += str((ta + tb + tc) % 2)
            tc = (ta + tb + tc) // 2
        if tc == 1: ans+='1'
        return ''.join(reversed(ans))
if __name__ == "__main__":
    x = Solution()
    a, b = "100110", "111111"
    print(x.addBinary(a, b))
    a, b = "1010", "1011"
    print(x.addBinary(a, b))
        