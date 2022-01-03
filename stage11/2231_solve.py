num = int(input())

for i in range(1, num):
    sum = i
    i_string = str(i)
    for j in range(len(i_string)):
        sum += int(i_string[j])

    if sum == num:
        gen = i
        break

else:
    gen = 0

print(gen)
