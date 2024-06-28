from itertools import permutations

def valid(num, d):
    num = int(num)
    return num % d == 0

def multiplos(n,d):
    count = 0
    for i in permutations([x for x in range(1, n+1)]):
        number = ""
        for num in i:
            number += str(num)
        if valid(int(number), d):
            count += 1
    return count

# 100 %