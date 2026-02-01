import sys
input = sys.stdin.readline

N = int(input())

result = []

for i in range(N // 4):
    result.append("long")

result.append("int")
print(" ".join(result))