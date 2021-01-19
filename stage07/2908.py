a, b = map(int, input().split())

rev_a = (a % 10) * 100 + ((a - (a // 100) * 100) // 10) * 10 + (a // 100) 
rev_b = (b % 10) * 100 + ((b - (b // 100) * 100) // 10) * 10 + (b // 100)

print(max(rev_a, rev_b))

# a, b = input().split()

# a = int(a[::-1])
# b = int(b[::-1])

# print(max(a, b))