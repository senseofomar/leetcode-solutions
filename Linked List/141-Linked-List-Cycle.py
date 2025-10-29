# Floyd’s Tortoise and Hare Algorithm (Most Optimal)
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next         # move 1 step
        fast = fast.next.next    # move 2 steps

        if slow == fast:         # they meet → cycle
            return True

    return False  # reached end → no cycle
