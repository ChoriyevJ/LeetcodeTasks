from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        pass


lst = ListNode(3, ListNode(4, ListNode(5)))
while True:
    print(lst.val)
    if not lst.next:
        break
    lst = lst.next



