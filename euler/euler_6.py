# Project Euler 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_squares(n):
  return sum([pow(x, 2) for x in range(n+1)])

def square_sum(n):
  return pow(sum(range(n+1)), 2)

def main():
  difference = square_sum(100) - sum_squares(100)
  print '{}'.format(difference)

if __name__ == '__main__':
  main()
