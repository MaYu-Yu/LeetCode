import os
import sys
from pathlib import Path

class Directory_Tree(object):
    def __init__(self, path, father_path, isLast):
        self.path = Path(str(path))
        self.father = father_path
        self.isLast = isLast
        if self.father:
            self.depth = self.father.depth + 1
        else:
            self.depth = 0
    
    @property
    def PREFIX_MID(self):
        return '├──'
    @property
    def PREFIX_LAST(self):
        return '└──'
    @property
    def F_PREFIX_MID(self):
        return '    '
    @property
    def F_PREFIX_LAST(self):
        return '│   '
    @property
    def display_name(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name
    
    @classmethod
    def create_tree(self, root, father=None, isLast=False):
        root_obj = self(root, father, isLast)
        yield root_obj

        son = sorted(list(path for path in root_obj.path.iterdir()), 
            key=lambda s: str(s).lower())
        count = 1
        for path in son:
            isLast = (count == len(son))
            if path.is_dir():
                yield from self.create_tree(path,
                    father=root_obj,
                        isLast=isLast)
            else:
                yield self(path, root_obj, isLast)
            count += 1

    def displayable(self):
        if self.father is None:
            return self.display_name
        
        if self.isLast:
            output = ["{!s} {!s}".format(
                self.PREFIX_LAST, self.display_name)]
        else:
            output = ["{!s} {!s}".format(
                self.PREFIX_MID, self.display_name)]

        father = self.father
        while father and father.father != None:
            if father.isLast:
                output.append(self.F_PREFIX_MID)
            else:
                output.append(self.F_PREFIX_LAST)
            father = father.father

        return ''.join(reversed(output))

if __name__ == "__main__":
    # input("輸入欲探索資料夾:")))
    paths = Directory_Tree.create_tree(r"D:\Coding\MySQL")
    for path in paths:
        print(path.displayable())
