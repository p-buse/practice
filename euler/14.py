"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

naive solution:
try every number, starting at 1 and counting up, counting its chain length

better:
try every number, starting at 1 and counting up, and saving the length to a map.
when we encounter a number whose length we've already calculated, we can use our map
value."""

lengths = {}


def collatz_length(num):
    n = num
    length = 1
    while n != 1:
        if n in lengths:
            length += lengths[n]
            lengths[num] = length
            return length
        length += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = n*3 + 1
    lengths[num] = length
    return length


def main():
    longest_num = -1
    longest_length = 0
    for i in range(1, 1000000):
        length = collatz_length(i)
        if length > longest_length:
            longest_num = i
            longest_length = length
    print(longest_num)


if __name__ == "__main__":
    main()
