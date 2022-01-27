class Solution(object):
    def plusOne(self, digits):
        carry_Flag = False
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                carry_Flag = True
            else:
                digits[i] += 1
                carry_Flag = False
                break
        if carry_Flag: digits.insert(0,1)
        return digits
if __name__ == "__main__":
    a = Solution()
    digits = [1,2,3]
    print(a.plusOne(digits))
    digits = [9,9,9,9]
    print(a.plusOne(digits))
    digits = [0]
    print(a.plusOne(digits))
        