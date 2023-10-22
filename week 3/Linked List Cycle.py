# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=b=head
        while(a!=None and a.next!=None):
            b=b.next
            a=a.next.next
            if(a==b):
                return True
        return False