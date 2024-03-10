from typing import Optional

from Medium.medium import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        simple_list1 = self.get_list(list1)
        print(f'simple_list1 = {simple_list1}')
        simple_list2 = self.get_list(list2)
        print(f'simple_list2 = {simple_list2}')
        extends_list = self.get_extends_list(simple_list1, simple_list2)
        print(f'extends_list = {extends_list}')
        self.mergeSort(extends_list)
        print(f'extends_list = {extends_list}')
        return self.get_list_node(extends_list)


    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = R[j]
                    j += 1
                    k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1


    def get_list(self, lst: Optional[ListNode]) -> list:
        result = []
        if lst.val == 0 and lst.next is None:
            while True:
                val = lst.val
                result.append(val)
                if not lst.next:
                    break
                lst = lst.next
        return result


    def get_extends_list(self, list1, list2):
        result = []
        for item in list1:
            result.append(item)
        for item in list2:
            result.append(item)
        return result


    def get_list_node(self, extends_list):
        result = ListNode()
        if len(extends_list) == 0:
            return []
        n = len(extends_list)
        i = 0
        while i < n:
            result.val = extends_list[n - 1 - i]
            l = result
            if i != n - 1:
                result = ListNode()
                result.next = l
            i += 1
        return result


l1 = ListNode()
l2 = ListNode()

arr = [7, 1, 0, 9, 4, 5, 2]
if __name__ == '__main__':
    sol = Solution().mergeTwoLists(l1, l2)
    print(sol.val, end=', ')
    if sol.next:
        print(sol.next.val, end=', ')
        if sol.next.next:
            print(sol.next.next.val, end=', ')
            if sol.next.next.next:
                print(sol.next.next.next.val, end=', ')
                if sol.next.next.next.next:
                    print(sol.next.next.next.next.val, end=', ')
                    if sol.next.next.next.next.next:
                        print(sol.next.next.next.next.next.val, end=', ')

