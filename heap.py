import random

class Heap:
    def __init__(self):
        # Start with an item in the heap so that 1-based swapping works.
        self.data = [None]
        self.size = 0

    def insert(self, value):
        self.data.append(value)
        self.size += 1
        pos = self.size
        while pos > 1 and self.data[pos] < self.data[pos // 2]:
            self._swap(pos, pos // 2)
            pos = pos // 2

    def pop(self):
        if self.size < 1:
            raise IndexError('No items to pop')
        ret = self.data[1]
        self.data[1] = self.data[self.size]
        del self.data[self.size]
        self.size -= 1
        self._percolate_up()
        return ret

    def _percolate_up(self):
        pos = 1
        while pos * 2 <= self.size:
            if pos * 2 == self.size:
                if self.data[pos] > self.data[pos * 2]:
                    self._swap(pos, pos*2)
                break
            elif self.data[pos] > self.data[pos * 2] or self.data[pos] > self.data[pos*2+1]:
                if self.data[pos*2] < self.data[pos*2+1]:
                    self._swap(pos, pos*2)
                    pos = pos * 2
                else:
                    self._swap(pos, pos*2+1)
                    pos = pos*2 + 1
            else:
                break


    def _swap(self, i, i2):
        if i > self.size or i2 > self.size:
            raise ValueError('Index cannot be higher than size')
        self.data[i], self.data[i2] = self.data[i2], self.data[i]

    def __str__(self):
        return str(self.data)


def main():
    h = Heap()
    things = [random.randint(0, 100) for _ in range(10)]
    for t in things:
        h.insert(t)

    for t in sorted(things):
        print('heap: {} sorted: {}'.format(h.pop(), t))


if __name__ == '__main__':
    main()
