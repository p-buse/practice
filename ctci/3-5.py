from random import randint

def stack_sort(stack):
    tmp = []
    for n in range(len(stack), 0, -1):
        sort_one(n, stack)

def sort_one(n, stack):
    mini = None
    tmp = []
    for _ in range(n):
        el = stack.pop()
        if mini is None or el < mini:
            mini = el
        tmp.append(el)
    stack.append(mini)
    while tmp:
        el = tmp.pop()
        if el == mini:
            mini = None
            continue
        stack.append(el)


def main():
    l = [randint(0, 100) for _ in range(10)]
    print(l)
    stack_sort(l)
    print(l)


if __name__ == '__main__':
    main()
