# Euler 9
# Find a, b, c, such that a^2 + b^2 = c^2 and a+b+c = 1000.
import itertools

def is_pythagorean(a, b, c):
  return pow(a, 2) + pow(b, 2) == pow(c, 2)

def main():
  number = 1000
  combinations = itertools.product(range(number), range(number), range(number))
  for a, b, c in combinations:
    if a + b + c != number:
      continue
    if not (a < b and b < c):
      continue
    if is_pythagorean(a, b, c):
      print 'a: {} b: {} c: {}'.format(a, b, c)
      print '{}'.format(a*b*c)
      return

if __name__ == '__main__':
  main()
