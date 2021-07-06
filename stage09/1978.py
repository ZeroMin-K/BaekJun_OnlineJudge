n = int(input())
numbers = map(int, input().split())

prime = 0
for num in numbers:
    is_not_prime = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                is_not_prime = True
                continue
        if is_not_prime is False:
            prime += 1

print(prime)
