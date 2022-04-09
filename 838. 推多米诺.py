# 擊敗100%!~~
class Solution(object):
    def pushDominoes(self, dominoes):
        print(dominoes)
        arr = []
        n = len(dominoes)
        base = -1
        for i in range(n):
            if dominoes[i] != '.':
                if base != -1:
                    if base == 0:
                        if dominoes[i] == 'L': # fall to left 
                            for j in range(base, i):
                                arr[j] = 'L'
                    else:
                        if dominoes[base - 1] == 'R':                       
                            if dominoes[i] == 'L': # balance
                                size = (i - base) // 2
                                for j in range(size):
                                    arr[base + j] = 'R'
                                    arr[i - j - 1] = 'L'
                            else: # fall to right
                                for j in range(base, i):
                                    arr[j] = 'R'
                        else:
                            if dominoes[i] == 'L': # fall to left
                                for j in range(base, i):
                                    arr[j] = 'L'         
                    base = -1
            else:
                if base == -1:
                    base = i
            arr.append(dominoes[i])
        if base > 0 and dominoes[base - 1] == 'R': # fall to right
            for j in range(base, n):
                arr[j] = 'R' 
        return "".join(arr) 
if __name__ == "__main__":
    a = Solution()
    dominoes = "RR.L"
    print(a.pushDominoes(dominoes))
    dominoes = ".L.R...LR..L.."
    print(a.pushDominoes(dominoes))
