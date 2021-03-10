from sys import stdin, stdout


def sieve(n):
    global primerange
    prime = [True for i in range(n+1)]
    prime[0] = prime[1] = False
    p = 2
    while(p*p <= n):
        if prime[p] == True:
            for i in range(p*p, n+1, p):
                prime[i] = False

        p += 1
    for i in range(len(prime)):
        if prime[i] == True:
            primerange.append(i)


for _ in range(int(stdin.readline())):
    primerange = []
    count = 0
    n = int(stdin.readline())
    sieve(n)
    for i in range(1, len(primerange)):
        if sum(primerange[:i+1]) in primerange:
            count += 1
    print(count)
