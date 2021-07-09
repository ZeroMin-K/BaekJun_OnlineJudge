import math 

def is_Prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

m,n = map(int, input().split()) 

for i in range(m, n+1):
    if is_Prime(i):
        print(i)
