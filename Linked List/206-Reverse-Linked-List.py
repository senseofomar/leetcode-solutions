#Iterative
def reverseList(self, head):
    prev = None  # initially nothing before head
    curr = head  # start with first node

    while curr:  # while not reached end
        nxt = curr.next  # temporarily save next node
        curr.next = prev  # reverse the link
        prev = curr  # move prev forward
        curr = nxt  # move curr forward

    return prev  # prev becomes new head