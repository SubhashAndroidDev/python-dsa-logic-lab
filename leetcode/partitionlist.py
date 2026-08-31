from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        less_head = ListNode(0)
        greater_head = ListNode(0)

        less = less_head
        greater = greater_head

        while head:

            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next

            head = head.next

        greater.next = None
        less.next = greater_head.next

        return less_head.next


# Create linked list:
# 1 -> 4 -> 3 -> 2 -> 5 -> 2

head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

x = 3

solution = Solution()
result = solution.partition(head, x)


# Print result
while result:
    print(result.val, end=" -> ")
    result = result.next

print("None")