# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

#快速排序法
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    sort1 = []
    sort2 = []
    while list1 is not None or list2 is not None:
        if list1 is not None:
            sort1.append(list1.val)
            list1 = list1.next
        if list2 is not None:
            sort2.append(list2.val)
            list2 = list2.next
    sort1.extend(sort2)
    output = quick_sort(sort1)
    head = ListNode(0)
    tail = head
    for i in output:
        tail.next = ListNode(i)
        tail = tail.next
    return head.next

#別人的code
"""
比對完之後讓他.next
因list1 and list2所以最後比較長的會剩下
所以需要tail.next = list1 或者 = list2
"""
def otherMergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    head = tail = ListNode(0)
    if list1 and list2:
        if list1.val < list2.val:
            tail.next = list1.val
            list1 = list1.next
        else:
            tail.next = list2.val
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return head.next
# 建立 l1: 9 -> 9 -> 9 -> 9 -> 9
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(4)

# 建立 l2: -> 9 -> 9 -> 9
b = ListNode(0)
"""b.next = ListNode(3)
b.next.next = ListNode(4)"""

print_linked_list(otherMergeTwoLists(None,b))