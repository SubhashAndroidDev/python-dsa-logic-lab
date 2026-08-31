class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode(0)
        current = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Add remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next


# Create List 1
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Create List 2
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)


# Merge
solution = Solution()
result = solution.mergeTwoLists(list1, list2)


# Print result
while result:
    print(result.val, end=" -> ")
    result = result.next

print("None")