x, y, z = map(int, input().split())
a = int(x)
b = int(y)
c = int(z)

print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c)) % c)