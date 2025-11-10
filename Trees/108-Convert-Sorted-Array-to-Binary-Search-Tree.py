# Define the binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums):
    # Base case: if the list is empty, no node to create
    if not nums:
        return None

    # Step 1: choose the middle element as the root
    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    # Step 2: recursively build left and right subtrees
    root.left = sorted_array_to_bst(nums[:mid])      # all elements before mid
    root.right = sorted_array_to_bst(nums[mid + 1:]) # all elements after mid

    return root
