import math
n = int(input())
numbers = list(map(int, input().split()))

xor = 0
array = []


def printDivisors(n):
    global array

    i = 1
    while i <= math.sqrt(n):

        if (n % i == 0):

            if (n / i == i):
                array.append(i)
            else:
                array.append(i)
                array.append(n//i)
        i = i + 1


for i in numbers:
    printDivisors(i)
for i in array:
    xor = xor ^ i

if xor == 0:
    print("JASBIR")
else:
    print("AMAN")

