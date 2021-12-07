class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        curr1 = l1
        curr2 = l2
    #設置Head
        if curr1.val < curr2.val:
            head = ListNode(curr1.val)
            curr1 = curr1.next
        else:  
            head = ListNode(curr2.val)
            curr2 = curr2.next
        curr = head

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:  
                curr.next = ListNode(curr2.val)
                curr2 = curr2.next
            curr = curr.next
        while curr1:
            curr.next = ListNode(curr1.val)
            curr1 = curr1.next
            curr = curr.next
        while curr2:
            curr.next = ListNode(curr2.val)
            curr2 = curr2.next
            curr = curr.next
        return head
def print_tree(head):
    while head:
        print(head.val, end='->')
        head = head.next
if __name__ == '__main__':
    a = Solution()
    s = ListNode(1)
    s.next = ListNode(2)
    s.next.next = ListNode(4)
    s0 = ListNode(1)
    s0.next = ListNode(3)
    s0.next.next = ListNode(4)
    print_tree(a.mergeTwoLists(s, s0))