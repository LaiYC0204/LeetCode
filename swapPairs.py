class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

#GPT幫忙
def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next: #確認可以交換
        return head

    # 交换前两个节点
    first = head
    second = head.next

    first.next = second.next
    second.next = first

    second.next.next = swapPairs(second.next.next)

    return second

listNode = ListNode(1)
listNode.next = ListNode(2)
listNode.next.next = ListNode(3)
listNode.next.next.next = ListNode(4)
listNode.next.next.next.next = ListNode(5)

print_linked_list(swapPairs(listNode))