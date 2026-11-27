from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
    def printList(self, head: ListNode | None):
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next
            
node3 = ListNode(3)
node2 = ListNode(2,node3)
node1 = ListNode(1,node2)
nodea = ListNode(0,node1)


print("Original list:")
Solution().printList(nodea)

# Reverse it
reversed_head = Solution().reverseList(nodea)

print("Reversed list:")
Solution().printList(reversed_head)