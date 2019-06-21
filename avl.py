class AVL:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self._height = -1


    @property
    def height(self):
        if self.left is None and self.right is None:
            return -1
        return self._height


    def update_height(self):
        self._height = 1 + max(self.left.height, self.right.height)


    def add(self, data):
        node = self
        while True:
            if data <= node.data:
                if node.left is None:
                    node.left = AVL(data)
                    node.left.parent = node
                    node = node.left
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = AVL(data)
                    node.right.parent = node
                    node = node.right
                    break
                else:
                    node = node.right
        if not node.is_balanced():
            node.rebalance()
        while node:
            node.update_height()
            node = node.parent


    def is_balanced(self):
        return abs(self.left.height - self.right.height) >= 1


    def rebalance(self, self):
        if self.right.height > self.left.height: # self is right-heavy
            if self.right.right.height > self.right.left.height:
                # case 1: right-right rebalance
                a, b, c = self, self.right, self.right.right
                t0, t1, t2, t3 = a.left, b.left, c.left, c.right
            else:
                # case 2: right-left rebalance
                a, b, c = self, self.right.left, self.right
                t0, t1, t2, t3 = a.left, b.left, b.right, c.right
        else: # self is left-heavy
            if self.left.right.height > self.left.left.height:
                # case 3: left-right rebalance
                a, b, c = self.left, self.left.right, self
                t0, t1, t2, t3 = a.left, a.right, b.right, c.right
            else:
                # case 4: left-left rebalance
                a, b, c = self.left.left, self.left, self
                t0, t1, t2, t3 = a.left, b.left, b.right, c.right

        newLeft = AVL(a.data)
        newLeft.left, newLeft.right = t0, t1
        newRight = AVL(c.data)
        newRight.left, newRight.right = t2, t3
        self.left, self.right = newLeft, newRight
        self.data = b.data
        self.update_height()
