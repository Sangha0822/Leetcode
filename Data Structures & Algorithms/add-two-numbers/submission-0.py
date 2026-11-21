# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        sum1 = 0
        cnt = 0
        while l1:
            sum1 = sum1 + (l1.val * pow(10,cnt))
            cnt += 1
            l1 = l1.next
        
        sum2 = 0
        cnt = 0
        while l2:
            sum2 = sum2 + (l2.val * pow(10,cnt))
            cnt += 1
            l2 = l2.next
        
        result = sum1 + sum2
        
        dummy = ListNode(0)
        curr = dummy
        
        while result > 0:
            digit = result % 10
            curr.next = ListNode(digit)
            curr = curr.next
            result = result // 10
        
        if dummy.next is None:
            return ListNode(0)
        return dummy.next