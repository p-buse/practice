# Multi-stack, in which the smaller stacks never get too big.

class Stacks:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError('Capacity must be greater than 0')
        self._capacity = capacity
        self._stacks = []

    def push(self, item):
        if not self._stacks:
            self._stacks.append([])
        if len(self._stacks[-1]) >= self._capacity:
            self._stacks.append([])
        self._stacks[-1].append(item)

    def pop(self):
        if not self._stacks:
            raise ValueError('No items to pop')
        item = self._stacks[-1].pop()
        if not self._stacks[-1]:
            self._stacks.pop()
        return item

    def __str__(self):
        return str(self._stacks)

def main():
    cap = 3
    n = 10
    S = Stacks(cap)
    for i in range(n):
        print(S)
        S.push(i)
    for i in range(n):
        print(S)
        S.pop()
    print(S)
    try:
        S.pop()
    except ValueError as e:
        print('error correctly raised: {}'.format(e))

if __name__ == '__main__':
    main()