dict = {}

for alpha in 'abcdefghijklmnopqrstuvwsxyz':
    dict[alpha] = -1

str = input()

i = 0
for alpha in str:
    if dict[alpha] == -1:
        dict[alpha] = i
    i += 1

for key in dict:
    print(dict[key], end= ' ')