# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                 tail.next = list1
                 list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next # <- pointer to initial tail
        # curr1 = list1
        # curr2 = list2
        # head = None
        # first = True
        
        # while curr1.next and curr2.next:
        #     while curr1.next and curr1.val <= curr2.val:
        #         if first:
        #             head = curr1
        #             first = False                    
        #         curr1 = curr1.next
        #     next1 = curr1.next
        #     curr1.next = curr2
        #     curr1 = next1
        #     while curr2.next and curr2.val < curr1.val:
        #         if first:
        #             head = curr2
        #             first = False                             
        #         curr2 = curr2.next
        #     next2 = curr2.next
        #     curr2.next = curr1
        #     curr2 = next2

    def listToLinkedList(self, nums: list[int]) -> ListNode | None:
        dummy = ListNode()          # fake node so you don't special-case the head
        tail = dummy
        for n in nums:
            tail.next = ListNode(n)
            tail = tail.next
        return dummy.next

    def linkedListToList(self, head: ListNode | None) -> list[int]:
        out = []
        while head:
            out.append(head.val)
            head = head.next
        return out
    
s = Solution()
l1 = s.listToLinkedList([1, 2, 4])
l2 = s.listToLinkedList([1, 3, 4])
print(s.linkedListToList(s.mergeTwoLists(l1, l2)))