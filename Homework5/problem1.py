cache = {}

def factorial_n(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    if n in cache:
        return cache[n]
    cache[n] = n * factorial_n(n-1)
    return cache[n]

n = 0

while int(n) >= 0:
    n =input('enter a natural number ')
    if n == 'exit':
        break
    if n!= 'exit':
        n = int(n)

    print(factorial_n(n))
       
