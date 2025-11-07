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