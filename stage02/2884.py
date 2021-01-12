h, m = map(int, input().split())
rest = m - 45
if m >= 45:
    print(h, rest)
else:
    if (h == 0):
        print(23, 60+ rest)
    else:   
        print(h-1, 60 + rest)


# 다른 답압
""" if m >= 45:
    m = m -45
else:
    if h >= 1:
        h = h-1
        m= m + 60 - 45
    else:
        h = h + 24 -1
        m = m + 60 -45
print(h, m) """