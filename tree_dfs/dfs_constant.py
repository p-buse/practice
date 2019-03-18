# A tree node.
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def add_child(self, name):
        child = Node(name)
        child.parent = self
        self.children.append(child)
        return child
    
def out(n):
    print(n.name)

# A DFS on a tree using O(1) space.
def dfs(n):
    last = None
    while n is not None:
        if len(n.children) == 0:
            out(n)
            last = n
            n = n.parent
        elif last in n.children:
            next = n.children.index(last) + 1
            if next < len(n.children):
                n = n.children[next]
            else:
                out(n)
                last = n
                n = n.parent
        else:
            n = n.children[0]

def example():
    a = Node('A')
    b = a.add_child('B')
    b.add_child('C')
    b.add_child('D')
    return a

def complex_example():
    a = Node('A')
    b = a.add_child('B')
    b.add_child('E')
    f = b.add_child('F')
    f.add_child('H')
    c = a.add_child('C')
    c.add_child('D')
    a.add_child('G')
    return a

def main():
    tree = complex_example()
    dfs(tree)

if __name__ == '__main__':
    main()
