from math import ceil, sqrt

divisors = {}

def main():
    n = 1
    num = 0
    while True:
        num += n
        nd = num_divisors(num)
        print('num: {} divisors: {}'.format(num, nd))
        if nd > 500:
            break
        n += 1
        
def num_divisors(num):
    if num == 1:
        return 1
    nd = 0
    for divisor in range(1, ceil(sqrt(num))):
        if divisor == sqrt(num):
            nd += 1
        elif num % divisor == 0:
            nd += 2
    return nd

if __name__ == '__main__':
    main()