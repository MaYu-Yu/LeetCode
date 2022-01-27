import collections
class Solution:
    def lengthOfLongestSubstring(self, s):
        aUsed = [False for _ in range(95)] # 已使用的字符list，ASCii可顯示字符編號範圍是32-126，共95個字符。
        aQueue = collections.deque() # 最長字串queue
        Maxlen = 0
        for a in s:
            a_index = ord(a)-32
            if aUsed[a_index]:
            # 發現重複字符，並比對最大長度
                l = len(aQueue)
                while aQueue != None: 
                # 於aQueue刪除重複字符前面的所有字符，並於aUsed將其設為未使用
                    temp = aQueue.popleft() 
                    aUsed[ord(temp) - 32] = False
                    if temp == a: break # 找到重複的字符了，跳出
                Maxlen = max(Maxlen, l)
        # aQueue加入該字符，並於aUsed將其設為已使用
            aQueue.append(a)
            aUsed[a_index] = True 
        Maxlen = max(Maxlen, len(aQueue)) # 最後沒有發現重複字符的最長字串
        return Maxlen
if __name__ == '__main__':
    a = Solution()
    word = " a"
    print(a.lengthOfLongestSubstring(word))