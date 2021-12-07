# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if k == 0 or not head or not head.next:
            return head
    # count size
        size = 1
        curr = head 
        while curr.next != None:
            size+=1
            curr = curr.next
        k = k % size
        if k == 0: return head
    # rotate
        pre = head
        curr = head
        while curr != None:
            if k == -1:
                pre.next = None
                prehead = head
                head = curr
            pre = curr
            curr = curr.next      
            k-=1  
        pre.next = prehead
        return head
def printNode(head):
    while head.next != None:
        print(head.val, end = '->')
        head = head.next
    print(head.val)
if __name__== "__main__":
    a = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    k = 2
    printNode(a.rotateRight(head, k))
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    k = 4
    printNode(a.rotateRight(head, k))
