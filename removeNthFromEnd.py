class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
    """
    current = head
    length = 0
    while current != None:
        length += 1
        current = current.next

    if length == 1:
        return None
    elif length == n:
        return head.next

    current = head
    for i in range(length):
        if i == length - n - 1:
            current.next = current.next.next
            break
        current = current.next

    return head

#快慢指針
def GPTremoveNthFromEnd(head, n):
    # 創建一個 dummy 節點，指向 head
    dummy = ListNode(0, head)
    fast = slow = dummy
    
    # 快指針先移動 n 步
    for _ in range(n):
        fast = fast.next
    
    # 快慢指針同時移動，直到快指針到達末尾
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    # 刪除慢指針的下一個節點
    slow.next = slow.next.next
    
    # 返回新的鏈表頭節點
    return dummy.next

listNode = ListNode(1)
listNode.next = ListNode(2)
listNode.next.next = ListNode(3)
listNode.next.next.next = ListNode(4)
listNode.next.next.next.next = ListNode(5)

tempListNode = GPTremoveNthFromEnd(listNode, 2)
print_linked_list(tempListNode)