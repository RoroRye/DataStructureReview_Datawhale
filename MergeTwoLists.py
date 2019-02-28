class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def MergeTwoLists(self, l1, l2):
        """
        l1: ListNode
        l2: ListNode
        return: ListNode
        """
        if l1 == None and l2 == None:
            return None
        NewList = ListNode(0)
        p = NewList
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1 != None:
            p.next = l1
        else:
            p.next = l2
        return NewList.next