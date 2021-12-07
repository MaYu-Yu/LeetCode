class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printList(head):
    print("NodeList is ", end="")
    while head:
        print(head.val, end="->")
        head = head.next
    print()
def setListNode():
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    return a

class Solution(object):
    def reverse(self, head, tail):
        pre = tail
        while head != tail:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
    def reverseKGroup(self, head, k):
        if not head or not head.next:
            return head
        tail = head
        for _ in range(0, k):
            if not tail: return head
            tail = tail.next
        newHead = self.reverse(head, tail)
        head.next = self.reverseKGroup(tail, k)
        return newHead
if __name__== "__main__":
    n = setListNode()
    n1 = setListNode()
    a = Solution()
    print("Q 1->2->3->4->5, k = 2")
    printList(a.reverseKGroup(n, 2))
    print("Q 1->2->3->4->5, k = 3")
    printList(a.reverseKGroup(n1, 3))
    print("Q 1, k = 1")
    printList(a.reverseKGroup(ListNode(1), 1))