from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words: return []
        s_size = len(s)
        one_word_size = len(words[0])
        words_size = len(words)
        if s_size < one_word_size * words_size: return []
        
        words = Counter(words)
        ans = []
        for i in range(0, one_word_size):
            success = 0
            curr_counter = Counter()
            l = r = i
            while r + one_word_size <= s_size:
                curr_word = s[r : r + one_word_size]
                r += one_word_size
                if curr_word in words: 
                    curr_counter[curr_word] +=1
                    success+=1
                    # 如果出現次數 > words的次數，就將 l 回到重複出現單字的第一次出現點，然後前面出現的清除不算。
                    while curr_counter[curr_word] > words[curr_word]:
                        temp_word = s[l : l + one_word_size]
                        curr_counter[temp_word] -=1
                        success-=1
                        l += one_word_size
                    if success == words_size: ans.append(l)   
                else:
                    l = r
                    success = 0
                    curr_counter.clear()
        return ans 
if __name__== "__main__":
    a = Solution()
    s, words = "lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]
    print(a.findSubstring(s, words))
    s, words = "barfoothefoobarman", ["foo","bar"] 
    print(a.findSubstring(s, words))
    s, words= "wordgoodgoodgoodbestword", ["word","good","best","word"]
    print(a.findSubstring(s, words))
    s, words= "barfoofoobarthefoobarman", ["bar","foo","the"]
    print(a.findSubstring(s, words))