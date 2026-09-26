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
        
        return dummy.next
            
        
        # #compare each curr , and have the smaller one point to the bigger one, then increment the smaller to the next node
        # head_1 = list1
        # head_2 = list2
        # start = head_1 if head_1 < head_2 else head_2
        
        # while head_1 or head_2:
        #     if not head_1.next: #we are on last note
        #         while head_2.val < head_1.val:
        #             head_2 = head_2.next
        #     if not head_2.next:
        #         while head_1.val < head_2.val:
        #             head_1 = head_1.next
        #     if head_1.val < head_2.val:
        #         next = head_1.next
        #         head_1.next = head_2
        #         head_1 = next
        #     else:
        #         next = head_2.next
        #         head_2.next = head_1
        #         head_2 = next
        # return start