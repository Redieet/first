# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 != None or l2 != None:
            x = l1.val if l1 != None else 0
            y = l2.val if l2 != None else 0
            carry = carry + x + y
            curr.val = carry % 10
            carry = carry // 10
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            if l1 != None or l2 != None:
                curr.next = ListNode(0)
                curr = curr.next
        if carry != 0:
            curr.next = ListNode(carry)
        return dummy