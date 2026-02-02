import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = list(map(int, sys.stdin.readline().split()))
    print(a + b)