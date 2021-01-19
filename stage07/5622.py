string = input()

total = 0

dict = {'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10}

for word in string:
    for key in dict:
        if word in key:
            total += dict[key]

print(total)