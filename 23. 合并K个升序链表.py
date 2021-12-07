class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printList(head):
    while head:
        print(head.val, end="->")
        head = head.next
def setListNode():
    alist = []
    a = ListNode(1)
    a.next = ListNode(4)
    a.next.next = ListNode(5)
    alist.append(a)
    a = ListNode(1)
    a.next = ListNode(3)
    a.next.next = ListNode(4)
    alist.append(a)
    a = ListNode(2)
    a.next = ListNode(6)
    alist.append(a)
    for i in alist:
        printList(i)
        print('')
    return alist

class Solution:
    def merge2List(self, list1, list2):
        head = ListNode()
        tail = head
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                list2 = list2.next
            tail = tail.next
        while list1: 
            tail.next = ListNode(list1.val)
            tail = tail.next
            list1 = list1.next
        while list2: 
            tail.next = ListNode(list2.val)
            tail = tail.next
            list2 = list2.next
        return head.next
    def mergeKLists(self, lists):
        length = len(lists)
        if length == 0:
            return ListNode().next
        times = 1
        while length > times :
            for i in range(0, length, 2*times):
                if i+times >= length: break
                lists[i] = self.merge2List(lists[i], lists[i+times])
            times*=2
        return lists[0]
if __name__ == '__main__':
    a = Solution()
    n = setListNode()
    print("result")
    printList(a.mergeKLists([]))
    printList(a.mergeKLists([[]]))
    printList(a.mergeKLists(n))