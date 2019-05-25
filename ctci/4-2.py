# Construct a BST of minimal height from an array of sorted integers.

def bst(arr):
    if len(arr) == 1:
        return Node(arr[0])
    if not arr:
        return None
    mid = len(arr) // 2
    node = Node(arr[mid])
    node.left = bst(arr[:mid])
    node.right = bst(arr[mid+1:])
    return node

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def main():
    arr = sorted([rand.randint(0,100) for _ in range(10)])
    b = bst(arr)

if __name__ == '__main__':
    main()
