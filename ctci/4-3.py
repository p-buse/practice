import collections

class Linked:
    def __init__(self):
        self._items = []

    def append(self, item):
        self._items.append(item)

    def length(self):
        return len(self._items)

    def __repr__(self):
        return '[' + ', '.join(map(str, self._items)) + ']'

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return self.data

    def __str__(self):
        return self.data


def depths(root):
    q = collections.deque([root, None])
    ret = []
    linked = Linked()
    while q:
        item = q.popleft()
        if item is None:
            if linked.length() > 0:
                ret.append(linked)
                linked = Linked()
            if q:
                q.append(None)
        else:
            linked.append(item)
            q.extend(c for c in (item.left, item.right) if c is not None)
    return ret


def main():
    root = BinaryTree('A')
    b = root.left = BinaryTree('B')
    c = root.right = BinaryTree('C')
    b.left = BinaryTree('D')
    b.right = BinaryTree('E')
    c.left = BinaryTree('F')
    c.right = BinaryTree('G')
    answer = depths(root)
    print(answer)

if __name__ == '__main__':
    main()
