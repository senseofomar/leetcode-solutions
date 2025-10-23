# Pointer Reversal Pattern
#Iterative
def reverse_list(self, head):
    prev = None  # initially nothing before head
    curr = head  # start with first node

    while curr:  # while not reached end
        nxt = curr.next  # temporarily save next node
        curr.next = prev  # reverse the link
        prev = curr  # move prev forward
        curr = nxt  # move curr forward

    return prev  # prev becomes new head

#Recursive
def reverse_list2(self, head):
    if not head or not head.next:
        return head

    new_head = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head