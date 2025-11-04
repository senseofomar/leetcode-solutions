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
        return is_mirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

    return is_mirror(root.left, root.right)