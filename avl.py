class AVL:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data
        self._height = -1


    @property
    def height(self):
        if self.left is None and self.right is None:
            return -1
        return self._height


    def update_height(self):
        self._height = max(self.left.height, self.right.height) + 1


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
        if not self.is_balanced():
            self.rebalance(node)
        self.update_height()


    def is_balanced(self):
        return abs(self.left.height - self.right.height) >= 1


    def rebalance(self, node):
        if node.right.height > node.left.height: # node is right-heavy
            if node.right.right.height > node.right.left.height:
                # case 1: right-right rebalance
                a, b, c = node, node.right, node.right.right
                t0, t1, t2, t3 = a.left, b.left, c.left, c.right
            else:
                # case 2: right-left rebalance
                a, b, c = node, node.right.left, node.right
                t0, t1, t2, t3 = a.left, b.left, b.right, c.right
        else: # node is left-heavy
            if node.left.right.height > node.left.left.height:
                # case 3: left-right rebalance
                a, b, c = node.left, node.left.right, node
                t0, t1, t2, t3 = a.left, a.right, b.right, c.right
            else:
                # case 4: left-left rebalance
                a, b, c = node.left.left, node.left, node
                t0, t1, t2, t3 = a.left, b.left, b.right, c.right

        newLeft = AVL(a.data)
        newLeft.left, newLeft.right = t0, t1
        newRight = AVL(c.data)
        newRight.left, newRight.right = t2, t3
        self.left, self.right = newLeft, newRight
        self.data = b.data
        self.update_height()