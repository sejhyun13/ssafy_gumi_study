import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = list(map(int, input().rstrip().split()))
    print(a+b)