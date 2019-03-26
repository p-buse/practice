import string
from timeit import timeit

filename = 'euler_8_input.txt'

def get_number():
  with open(filename, 'r') as f:
    return f.read().translate(None, string.whitespace)

def multiply(s):
  return reduce(lambda x, y: x*y, s)

def largest_product(num_digits, s):
  largest = 0
  numbers = ''
  lo, hi = 0, num_digits
  while hi < len(s):
    substr = s[lo:hi]
    product = multiply([int(x) for x in substr])
    if product > largest:
      largest = product
      numbers = substr
    lo, hi = lo+1, hi+1
  return largest, numbers

def largest_product_opt(num_digits, s):
  largest = 0
  numbers = ''
  substr = s[0:num_digits]
  product = multiply([int(x) for x in substr])
  lo, hi = 1, num_digits+1
  while hi < len(s):
    last_digit = int(s[lo-1])
    if last_digit != 0:
      product = (product / last_digit) * int(s[hi])
    else:
      product = 0
    if product > largest:
      largest = product
      numbers = substr
    lo, hi = lo+1, hi+1
  return largest, numbers


def main():
  num = 13
  iterations = 1000
  s = get_number()
  norm = lambda: largest_product(num, s)
  opt = lambda: largest_product_opt(num, s)
  print 'first iteration: {}'.format(timeit(norm, number=iterations))
  print 'second iteration: {}'.format(timeit(opt, number=iterations))
  # print 'largest product of length-{} subsequence: {}, with digits {}'.format(num, largest, numbers)

main()
