"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

def divisor_sum(n):
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return total


def divisor_sums(maximum):
    ret = {}
    n = 0
    while n < maximum:
        n += 1
        ds = divisor_sum(n)
        if ds < maximum:
            ret[n] = ds
    return ret


def main():
    maximum = 10000
    ds = divisor_sums(maximum)    
    total = 0
    for k, v in ds.items():
        if k != v and v in ds and ds[v] == k:
            total += k
    print(total)


if __name__ == '__main__':
    main()