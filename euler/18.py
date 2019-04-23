triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None


def parse_triangle(triangle):
    triangle = [[Node(int(n)) for n in r.split()]
                for r in triangle.splitlines()]
    for i in range(len(triangle) - 1):
        row = triangle[i]
        for j, node in enumerate(row):
            node.left = triangle[i+1][j]
            node.right = triangle[i+1][j+1]
    return triangle[0][0]


def find_greatest_path(node):
    if node.is_leaf():
        return node.val
    return node.val + max(find_greatest_path(node.left), find_greatest_path(node.right))


def main():
    t = parse_triangle(triangle)
    print(find_greatest_path(t))


if __name__ == '__main__':
    main()
