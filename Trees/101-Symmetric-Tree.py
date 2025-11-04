# Recursive DFS Solution (Most Common)
def is_symmetric(root) -> bool:
    if not root:
        return True

    def is_mirror(t1, t2):
        # both nodes are None → symmetric
        if not t1 and not t2:
            return True
        # one is None → asymmetric
        if not t1 or not t2:
            return False
        # values differ → asymmetric
        if t1.val != t2.val:
            return False

        # check mirror of subtrees
        return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

    return is_mirror(root.left, root.right)


from collections import deque


def is_symmetric2(root) -> bool:
    if not root:
        return True

    queue = deque([(root.left, root.right)])

    while queue:
        t1, t2 = queue.popleft()
        if not t1 and not t2:
            continue
        if not t1 or not t2 or t1.val != t2.val:
            return False

        # mirror pairing
        queue.append((t1.left, t2.right))
        queue.append((t1.right, t2.left))

    return True
