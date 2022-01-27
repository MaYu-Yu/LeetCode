class Solution(object):
    def simplifyPath(self, path):
        names = path.split("/")
        stack = list()
        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)
        return "/" + "/".join(stack)
if __name__ == "__main__":
    a = Solution()
    path = "//home//"
    print(a.simplifyPath(path))
    path = "/../"
    print(a.simplifyPath(path))
    path = "/home//foo/"
    print(a.simplifyPath(path))
    path = "/a/./b/../../c/"
    print(a.simplifyPath(path))
    
    