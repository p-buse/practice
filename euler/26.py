def find_cycle(n):
    found = set()
    num = 1
    while True:
        num *= 10
        rem = num % n
        # Number terminates
        if rem == 0:
            return 0
        if rem in found:
            return len(found)
        found.add(rem)
        num -= (num // n) * n

def main():
    d = 0
    longest = 0
    for i in range(1, 1000):
        cycle_len = find_cycle(i)
        if cycle_len > longest:
            d = i
            longest = cycle_len
    print(d)


if __name__ == '__main__':
    main()