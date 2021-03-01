weight = int(input())

for num_3 in range((weight // 3) + 1):
    for num_5 in range( (weight // 5) + 1):
        if ((5 * num_5 + 3 * num_3) == weight):
            print(num_3+ num_5)
            exit()

print(-1)
