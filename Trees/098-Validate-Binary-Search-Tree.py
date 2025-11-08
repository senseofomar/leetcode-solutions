# Recursive Range Check Solution
def is_valid_bst(root) -> bool:
    def helper(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True

        val = node.val
        # check current node
        if val <= low or val >= high:
            return False

        # check left subtree (values < node.val)
        if not helper(node.left, low, val):
            return False

        # check right subtree (values > node.val)
        if not helper(node.right, val, high):
            return False

        return True

    return helper(root)


# Inorder Traversal Solution
def is_valid_bst1(root) -> bool:
    prev = float('-inf')

    def inorder(node):
        nonlocal prev  # allows modifying outer variable
        if not node:
            return True

        # Left subtree
        if not inorder(node.left):
            return False

        # Current node check
        if node.val <= prev:
            return False
        prev = node.val

        # Right subtree
        return inorder(node.right)

    return inorder(root)

