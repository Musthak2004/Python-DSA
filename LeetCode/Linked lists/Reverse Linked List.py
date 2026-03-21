# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # 1. store next
            curr.next = prev        # 2. reverse pointer
            prev = curr             # 3. move prev
            curr = next_node        # 4. move curr

        return prev


# --------- TESTING CODE ---------

# Create Linked List: 1 -> 2 -> 3 -> 4 -> 5
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Reverse it
obj = Solution()
new_head = obj.reverseList(n1)

# Print reversed list
temp = new_head
while temp:
    print(temp.val)
    temp = temp.next