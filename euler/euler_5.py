# Project Eueler 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def divisible_by(n, num):
  for x in range(1, n+1):
    if num % x != 0:
      return False
  return True

def main():
  num = 20
  while True:
    if divisible_by(20, num):
      print 'found: {}'.format(num)
      break
    num += 20

if __name__ == '__main__':
  main()
