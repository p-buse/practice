# Project Euler #4
# Find the largest palindrome made from the product of two 3-digit numbers.
def gen_numbers():
  for i in range(999, 100 - 1, -1):
    for j in range(999, i-1, -1):
      yield str(i * j)

def is_palindrome(num):
  if len(num) <= 1:
    return True
  elif num[0] != num[-1]:
    return False
  return is_palindrome(num[1:-1])

def is_palindrome2(num):
  original_num = num
  reversed_num = 0
  while num:
    reversed_num = 10*reversed_num + (num % 10)
    num /= 10
  return original_num == reversed_num

def fast_palindromes():
  largest_palindrome = 0
  a = 999
  while a >= 100:
    if a % 11 == 0:
      b = 999
      db = 1
    else:
      b = 990 # Largest number <= 999 and divisible by 11
      db = 11
    while b >= a:
      num = a*b
      if num <= largest_palindrome:
        break
      if is_palindrome(str(num)):
        largest_palindrome = num
      b -= db
    a -= 1
  return largest_palindrome


def main():
  print '{}'.format(fast_palindromes())

if __name__ == '__main__':
  main()
