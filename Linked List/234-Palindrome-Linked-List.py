#Fast and slow pointers
def is_palindrome(self, head):
    if not head or not head.next:
        return True

    # Step 1: Find middle (slow will end up in middle)
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    # Now, prev is the head of the reversed half

    # Step 3: Compare first and second half
    first, second = head, prev
    while second:  # only need to check second half
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True