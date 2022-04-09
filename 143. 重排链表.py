# Definition for singly-linked list.
class Listp(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        if not head:
            return
        
        node_list = list()
        p = head
        while p:
            node_list.append(p)
            p = p.next
        
        i, j = 0, len(node_list) - 1
        while i < j:
            node_list[i].next = node_list[j]
            i += 1
            if i == j:
                break
            node_list[j].next = node_list[i]
            j -= 1
        
        node_list[i].next = None