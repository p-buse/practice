# Given an in-order and pre-order traversal of a binary tree,
# reconstruct the tree.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return '{}: ({}, {})'.format(self.data, str(self.left), str(self.right))

def tree_unwind(inorder, preorder):
    if not inorder or not preorder:
        return None
    # Grab root from preorder traversal
    root = preorder[0]
    # Find root in inorder traversal
    root_index = inorder.index(root)
    # Separate list into left and right and recurse
    root_node = Node(root)
    root_node.left = tree_unwind(inorder[:root_index], preorder[1:1+root_index])
    root_node.right = tree_unwind(inorder[root_index + 1:], preorder[1+root_index:])
    return root_node

def main():
    inorder = ['d', 'b', 'e', 'a', 'c']
    preorder = ['a', 'b', 'd', 'e', 'c']
    tree = tree_unwind(inorder, preorder)
    print(tree)

if __name__ == '__main__':
    main()
