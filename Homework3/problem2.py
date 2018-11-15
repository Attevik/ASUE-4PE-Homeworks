a = int(input ( "Enter a positive number. "))

def check(num):
    for n in range(2, num):
        if num%n == 0:
            return False
    return True

def primes_till(num):
    if num > 1:
        for e in range(2, num+1):
            if check(e):
                print(e, end=' ')
            
primes_till(a)
