class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    isfirst = False
    while l1!=None or l2!=None:    
        if l1 == None:
            sum = l2.val + carry
        elif l2 == None:
            sum = l1.val + carry
        else:
            sum = l1.val + l2.val + carry
        carry = 0
        if sum >= 10:
            carry=1
            sum-=10
        if isfirst: 
            curr.next = ListNode(sum)
            curr = curr.next
        else:  
            head = ListNode(sum)
            curr = head
            isfirst = True
        if l1 != None: l1 = l1.next
        if l2 != None: l2 = l2.next
    if carry == 1:
        curr.next = ListNode(1)
    return head
if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
#--print--
    head = addTwoNumbers(l1, l2)
    curr = head 
    while curr!=None:
        print(curr.val)
        curr = curr.next