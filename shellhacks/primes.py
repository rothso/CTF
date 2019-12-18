# What is the sum of the first 10,000 prime numbers between
# 1000 and 1,000,000 that end with the number 9

import re

f = open('input.txt', 'r')
primes = list(map(int, re.split(r'\s+', f.read())))

primes_in_range = [prime for prime in primes if prime > 1000 and prime < 1000000 and prime % 10 == 9]
ten_thousand_primes = primes_in_range[:10000]
total = sum(ten_thousand_primes)

print(total, len(ten_thousand_primes))