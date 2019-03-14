def running_sieve(n):
  primes = [2]
  num = 3
  while len(primes) < n:
    isPrime = True
    for prime in primes:
      if num % prime == 0:
        isPrime = False
        break
    if isPrime == True:
      primes.append(num)
    num += 2
  return primes

def main():
  num_primes = 10001
  print 'first {} primes'.format(num_primes)
  print '{}'.format(running_sieve(num_primes))

if __name__ == '__main__':
  main()
