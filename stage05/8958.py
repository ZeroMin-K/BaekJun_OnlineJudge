count = int(input())
sum = 0
score= 0
again = False

for _ in range(count):
    str = input()

    for i in range(len(str)):
        
        if str[i] == 'O':
            if again:
                score += 1
            else:
                score = 1
            
            sum += score
            again = True 
        else:
            again = False

    print(sum)
    sum = 0
    score = 0
