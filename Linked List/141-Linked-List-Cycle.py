# Floyd’s Tortoise and Hare Algorithm (Most Optimal)
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next         # move 1 step
        fast = fast.next.next    # move 2 steps

        if slow == fast:         # they meet → cycle
            return True

    return False  # reached end → no cycle

# HashSet Method (Simpler but not optimal)
def has_cycle1(head):
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False