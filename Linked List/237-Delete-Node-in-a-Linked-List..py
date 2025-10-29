def delete_node(node):
    node.val = node.next.val  # Copy next node’s value
    node.next = node.next.next  # Skip over the next node