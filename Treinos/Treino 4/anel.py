def get_this_index(list, num):
    for i in range(len(list)):
        if(list[i] == num):
            return i
    return -1

def next(n, candidate, index2change):

    if(candidate[index2change] == 1):
        index = get_this_index(candidate, n)
        candidate[index] = 1
        candidate[index2change] = n
    else:
        index = get_this_index(candidate, candidate[index2change] - 1)
        candidate[index] = candidate[index2change]
        candidate[index2change] -= 1
    return candidate

def is_not_prime(sum):
    for i in range(sum - 1, 1, -1):
        if(sum % i == 0):
            return True
    return False

def valid(n, candidate):

    if is_not_prime(candidate[0] + candidate[-1]):
        return False
    
    for i in range(n - 1):
        if is_not_prime(candidate[i] + candidate[i+1]):
            return False

    return True

def search(n, candidate):

    if(valid(n, candidate)):
        return candidate

    index2change = n - 1

    while(True):
        for times in range(n * (n - 1) - 1):
            if(valid(n, candidate)):
                return candidate
            candidate = next(n, candidate, index2change)
            print(candidate)
        index2change -= 1

def anel(n):
    if(n == 0):
        return 0
    return search(n, [x + 1 for x in range(n)])

# 50 % 