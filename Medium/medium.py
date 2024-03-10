from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:

        lst1 = self.add_to_list(l1)
        lst2 = self.add_to_list(l2)
        result = []
        dval = 0
        i = 0

        while True:
            if i < len(lst1) and i < len(lst2):
                n = len(lst2)
                if len(lst1) > len(lst2):
                    n = len(lst1)
                val = lst1[i] + lst2[i] + dval
                t = self.check_val(val)
                val = t[0]
                dval = t[1]
                result.append(val)
                self.append_last_dval(n, i, result, dval)

            elif i < len(lst1):
                val = lst1[i] + dval
                t = self.check_val(val)
                val = t[0]
                dval = t[1]
                result.append(val)
                self.append_last_dval(len(lst1), i, result, dval)
            elif i < len(lst2):
                val = lst2[i] + dval
                t = self.check_val(val)
                val = t[0]
                dval = t[1]
                result.append(val)
                self.append_last_dval(len(lst2), i, result, dval)
            else:
                break
            i += 1
        return self.return_list_node(result)

    def add_to_list(self, lst: Optional[ListNode]) -> list:
        result = []
        while True:
            result.append(lst.val)
            if not lst.next:
                break
            lst = lst.next
        return result

    def return_list_node(self, lst: list) -> Optional[ListNode]:
        result = ListNode()
        i = 0
        n = len(lst)
        while i < n:
            result.val = lst[n - 1 - i]
            l = result
            if i != n - 1:
                result = ListNode()
                result.next = l
            i += 1
        return result


    def check_val(self, val: int) -> tuple:
        if val >= 10:
            dval = 1
            if val == 10:
                val = 0
            else:
                val %= 10
        else:
            dval = 0
        return val, dval

    def append_last_dval(self, n, i, result, dval):
        if dval == 1 and i == n - 1:
            result.append(dval)



# lst1 = ListNode(8, ListNode(3, ListNode(2)))
# lst2 = ListNode(9, ListNode(2, ListNode(1)))

lst1 = ListNode(2, ListNode(4, ListNode(9)))
lst2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
if __name__ == '__main__':
    sol = Solution().addTwoNumbers(lst1, lst2)
    print(sol.val)
    if sol.next:
        print(sol.next.val)
        if sol.next.next:
            print(sol.next.next.val)
            if sol.next.next.next:
                print(sol.next.next.next.val)
                if sol.next.next.next.next:
                    print(sol.next.next.next.next.val)
                    if sol.next.next.next.next.next:
                        print(sol.next.next.next.next.next.val)



