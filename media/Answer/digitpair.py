from collections import Counter
import math
for _ in range(int(input())):
    n = int(input())
    numbers = list(input().split())
    bit = []
    # print(numbers)
    for i in numbers:
        max_ = int(max(i))
        min_ = int(min(i))
        a = max_*11 + min_*7
        a = str(a)
        if len(a) == 2:
            a = int(a)//10
            bit.append(a)
        else:
            a = a[-2:]
            a = int(a)//10
            bit.append(a)
    # print(bit)
    count = 0
    even = []
    odd = []
    for i in range(0, len(bit)):
        if i % 2 == 0:
            even.append(bit[i])
        else:
            odd.append(bit[i])
    dict1 = Counter(even)
    dict2 = Counter(odd)
    allvalue = dict1.values()
    max1 = max(allvalue)
    allvalue = dict2.values()
    max2 = max(allvalue)

    count = max2+max1
    # print(count)
    print(math.ceil(count/2))
