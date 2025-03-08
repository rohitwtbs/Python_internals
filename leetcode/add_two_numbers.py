# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        next = l1
        next2 = l2
        return_ll = ListNode(None , None)
        head = return_ll
        # print(return_ll)
        # print(return_ll.val)
        quiotent = 0
        last_node = None
        while next != None or next2 != None:
            # print(next.val)
            # add = (next.val + next2.val +) / 10
            if(next != None):
                val = next.val
            else:
                val = 0
            if(next2 != None):
                val2 = next2.val
            else:
                val2 = 0
            if(next != None  or next2 != None):
                quiotent,remainder = divmod(val + val2 + quiotent, 10)
            else:
                pass   
            return_ll.val = remainder
            # print(remainder)

            if(next != None):
                next = next.next
            if(next2 != None):
                next2 = next2.next
            if(next != None):
                n = ListNode()
                return_ll.next = n
                return_ll = n
            # print("execute")
            last_node = return_ll
        if(quiotent != 0 and return_ll != None):
            last_node.next = ListNode(quiotent , None)
        return head
        while(head.next != None):
            print(head.val)
            print(head.next)
            head = head.next
