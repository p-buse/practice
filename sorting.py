from collections import deque

def merge_sort(l):
    if len(l) == 1:
        return l
    lo = merge_sort(l[:len(l)//2])
    hi = merge_sort(l[len(l)//2:])
    merged = deque()
    while lo or hi:
        if lo and hi:
            if lo[-1] > hi[-1]:
                el = lo.pop()
            else:
                el = hi.pop()
        elif lo:
            el = lo.pop()
        else:
            el = hi.pop()
        merged.appendleft(el)
    return list(merged)



def main():
    l = [4, 140, 0, 1222, 5, -129, -3493, 3]
    s = sorted(l)
    print(l)
    print(s)
    if s != bubble(l):
        print('bubble differs')
        print(bubble(l))
    if s != merge_sort(l):
        print('merge differs')
        print(merge_sort(l))

if __name__ == '__main__':
    main()