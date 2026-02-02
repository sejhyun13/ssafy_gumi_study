T = int(input())

for _ in range(1, T+1):
    a, b = list(map(int, input().split()))
    print(f'Case #{_}: {a+b}')