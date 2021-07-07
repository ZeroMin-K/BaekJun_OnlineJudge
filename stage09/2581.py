m = int(input())
n = int(input())

prime_list = list()

for num in range(m, n+1):
    is_not_prime = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                is_not_prime = True
                break
    
        if is_not_prime is False:
            prime_list.append(num)

if len(prime_list) > 0:
    print(sum(prime_list))
    print(min(prime_list))
else:
    print(-1)
