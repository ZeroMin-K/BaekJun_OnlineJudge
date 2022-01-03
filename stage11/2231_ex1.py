n = int(input())

for i in range(1, n):
    num = list(map(int, str(i)))
    sum = i + sum(num)
    if sum == n:
        print(n)
        break
else:
    print(0)
