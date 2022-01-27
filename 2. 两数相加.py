class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self,l1, l2):
        carry = 0
        isfirst = True
        while l1 != None or l2 != None: 
        # 兩數相加
            if l1 == None:
                sum = l2.val + carry
            elif l2 == None:
                sum = l1.val + carry
            else:
                sum = l1.val + l2.val + carry
            carry = sum // 10
        # Node建立
            if isfirst: 
                head = ListNode(sum % 10)
                curr = head
                isfirst = False
            else:  
                curr.next = ListNode(sum % 10)
                curr = curr.next
            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next
    # 最後的進位記得別忘記~
        if carry == 1:
            curr.next = ListNode(1)
        return head
if __name__ == '__main__':
# setting node
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    a = Solution()
    head = a.addTwoNumbers(l1, l2)
# --print--
    curr = head 
    while curr!=None:
        print(curr.val)
        curr = curr.next