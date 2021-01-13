import sys

rep = int(sys.stdin.readline().rstrip())

for i in range(rep):
    input = sys.stdin.readline().rstrip()
    a, b = map(int, input.split())
    print(a+b)