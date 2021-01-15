case = int(input())
num_list = []


for _ in range(case):
    num_list = list(map(int, input().split()))
    students_count = num_list[0]
    del num_list[0]
    avg = sum(num_list) / students_count
    avg_count = 0

    for student in num_list:
        if student > avg:
            avg_count += 1

    print('{:.3f}%'.format(avg_count / students_count * 100))
