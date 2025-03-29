# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next  # Return the head of the linked list


class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        arr = []
        number1 = ""
        number2 = ""
        while l1 is not None:
            arr.append(l1.val)
            l1 = l1.next
        for value in reversed(list(map(str, arr))):
            number1 += value
        number1 = int(number1)

        arr.clear()

        while l2 is not None:
            arr.append(l2.val)
            l2 = l2.next

        for value in reversed(list(map(str, arr))):
            number2 += value
        number2 = int(number2)

        result = number1 + number2
        result = str(result)
        dummy = ListNode()
        l3 = dummy
        for char in reversed(result):
            l3.next = ListNode(int(char))
            l3 = l3.next
        return dummy.next


# l1 = create_linked_list([2, 4, 3])
# l2 = create_linked_list([5, 6, 4])

# sol = Solution()
# result = sol.addTwoNumbers(l1, l2)
