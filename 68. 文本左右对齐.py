class Solution(object):
    def fullJustify(self, words, maxWidth):
        ans = []
        one_str_words = []
        max_len = maxWidth
        s = ''
    # get len
        for word in words:
            if max_len > len(word) + 1:
                max_len -= len(word) + 1
            elif max_len == len(word) + 1:
            
            else:
                
        for word in words:
            
        return ans
if __name__ == "__main__":
    a = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(a.fullJustify(words, maxWidth))
    words = ["Science","is","what","we","understand","well","enough","to","explain", \
        "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    print(a.fullJustify(words, maxWidth))