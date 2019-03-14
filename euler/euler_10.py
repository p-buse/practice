# Find the sum of all primes below 2 million.

def primes(magic):
  numbers = [True for x in range(magic+1)]
  prime = 2
  while prime < magic:
    for remove_index in range(prime, magic, prime):
      numbers[remove_index] = False
    yield prime
    while not numbers[prime]:
      prime += 1

def main():
  number = int(2e6)
  total = 0
  for prime in primes(number):
    total += prime
  print '{}'.format(total)

if __name__ == '__main__':
  main()
