n = int(input())

sum = 1
i = 1

while True:
    if n <= sum:
        break
    i += 1
    sum += i

max_row = i
total = sum - i + 1
diff = n - total

if max_row % 2 == 1:
    row = max_row - diff
    col = diff + 1
else:
    col = max_row - diff
    row = diff + 1

print(f'{row}/{col}')
