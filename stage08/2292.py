n = int(input())

min = 1
max = 1
i = 0
while True:

    if  min <= n <= max:
        count = i + 1
        break

    i += 1
    min = max + 1
    max += 6 * i

print(count)
