# BFS with Queue (Iterative)

from collections import deque

def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])  # start with root node in queue

    while queue:
        level = []
        for _ in range(len(queue)):  # process all nodes in the current level
            node = queue.popleft()
            level.append(node.val)

            # Add children to the queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)  # add current level to result

    return result
