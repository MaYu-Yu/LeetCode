from debug import debug_class
DEBUG = debug_class(True)
class Solution:
    def groupAnagrams(self, strs):
        import collections
        mp = collections.defaultdict(list)
        # mp = dict()
        for st in strs:
            counts = [0 for _ in range(26)]
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            mp[tuple(counts)].append(st)
            # if tuple(counts) in mp:
            #     mp[tuple(counts)].append(st)
            # else:
            #     mp.update({tuple(counts): []})
            #     mp[tuple(counts)].append(st)
        return [mp[i] for i in mp]

if __name__== "__main__":
    a = Solution()
    strs = [["eat","tea","tan","ate","nat","bat"],
[""],
["a"]]
    for i in strs:
        print(a.groupAnagrams(i))