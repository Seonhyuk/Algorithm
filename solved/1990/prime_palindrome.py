def reverse(text):
    result = ''
    for t in text:
        result = t + result
    return result


n, m = map(int, input().split())
if m >= 10000000:
    m = 10000000
if 1000000 >= m >= 100000:
    m = 100000
if 10000 >= m >= 1000:
    m = 1000

primes = [False] + [True] * (m//2)
for i in range(1, len(primes)):
    if primes[i]:
        if i*2 + 1 >= n and str(i*2+1) == reverse(str(i*2+1)):
            print(2*i+1)
        for j in range(i + (2*i+1), len(primes), 2*i+1):
            primes[j] = False
print(-1)