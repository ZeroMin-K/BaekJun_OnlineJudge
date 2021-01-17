a, b = input().split()

rev_a = int(a[-1:3])
rev_b = int(b[-1:3])
print(rev_a, rev_b)


if rev_a > rev_b:
    print(rev_a)
else:
    print(rev_b)