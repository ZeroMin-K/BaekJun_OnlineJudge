x, y = map(int, input().split())
a = int(x)
b = int(y)

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')
