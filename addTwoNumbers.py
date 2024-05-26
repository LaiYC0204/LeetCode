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

def myAddTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    output = []
    carry = 0
    while(True):
        if(l1 is not None and l2 is not None):
            total = l1.val + l2.val + carry
            carry = total // 10
            output.append(ListNode(total % 10))
            l1 = l1.next
            l2 = l2.next
        elif(l1 is not None):
            total = l1.val + carry
            carry = total // 10
            output.append(ListNode(total % 10))
            l1 = l1.next
        elif(l2 is not None):
            total = l2.val + carry
            carry = total // 10
            output.append(ListNode(total % 10))
            l2 = l2.next
        else:
            if(carry != 0):
                output.append(ListNode(carry))
            break

    for i in range(len(output) -1):
        output[i].next = output[i + 1]
    return output[0]

# 建立 l1: 9 -> 9 -> 9 -> 9 -> 9
a = ListNode(9)
a.next = ListNode(9)
a.next.next = ListNode(9)
a.next.next.next = ListNode(9)
a.next.next.next.next = ListNode(9)

# 建立 l2: -> 9 -> 9 -> 9
b = ListNode(9)
b.next = ListNode(9)
b.next.next = ListNode(9)

listnode = myAddTwoNumbers(a,b)