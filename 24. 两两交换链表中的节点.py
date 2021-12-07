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
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head
        return temp
if __name__== "__main__":
    n = setListNode()
    a = Solution()
    print("Q []")
    printList(a.swapPairs(None))
    print("Q 1")
    printList(a.swapPairs(ListNode(1)))
    print("Q 1->2->3->4->5")
    printList(a.swapPairs(n))