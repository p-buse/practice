# Check if a tree is balanced. I.e. if the heights of the subtrees of each
# node differ by at most 1.

def is_balanced(node):
    if node is None:
        return True
    height_l = height(node.left)
    height_r = height(node.right)
    if abs(height_l - height_r) > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

# We can speed this up by precomputing the heights, instead of recomputing them
# for each node's is_balanced check.
