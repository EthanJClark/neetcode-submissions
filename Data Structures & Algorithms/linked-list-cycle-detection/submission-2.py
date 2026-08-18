# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}

        curr = head

        while curr:
            vis_val = visited.setdefault(curr, 0)
            if vis_val == 0:
                visited[curr] += 1
            else:
                return True            
            curr = curr.next

        return False