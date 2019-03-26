class AVL:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data
        self.height = 0

    def add(self, data):
        node = self
        while True:
            if data <= node.data:
                if node.left is None:
                    node.left = AVL(data)
                    node.left.parent = node
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = AVL(data)
                    node.right.parent = node
                    break
                else:
                    node = node.right
        self.rebalance(node)
        self.height = max(self.left.height, self.right.height) + 1


    def rebalance(self, node):
        if node.right.height > node.left.height: # node is right-heavy
            if node.right.right.height > node.right.left.height:
                # case 1: right-right rebalance
                pass
            else:
                # case 2: right-left rebalance
                pass
        else: # node is left-heavy
            if node.left.right.height > node.left.left.height:
                # case 3: left-right rebalance
                pass
            else:
                # case 4: left-left rebalance
                pass

