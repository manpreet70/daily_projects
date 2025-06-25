# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        tail = current = ListNode()
        carry_over = 0
        

        while l1 or l2 or carry_over:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry_over, val = divmod((val1 + val2 + carry_over),10)
            tail.next = ListNode(val)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            
        # No need to use If separately. Include Carry in the while loop.    
            # if carry_over:
            #     tail.next = ListNode(carry_over)
        
        return current.next



