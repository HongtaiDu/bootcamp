# I was not able to solve this question, so I used one of the solution on leetcode

#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for (i, head) in enumerate(lists):
            if head:
                heappush(pq, (head.val, i, head))
        temp = ListNode()
        tail = temp
        while pq:
            _, i, node = heappop(pq)
            tail.next = node
            tail = node
            if node.next:
                heappush(pq, (node.next.val, i, node.next))
        return temp.next