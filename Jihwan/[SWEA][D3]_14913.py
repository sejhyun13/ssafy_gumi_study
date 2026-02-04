# 문제: 다음 100X100의 2차원 배열이 주어질 때, 
# 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

def lst_sum(lst): # 리스트 sum함수 
    result = 0
    for i in lst:
        result += i
    return result
 
def line_sum(arr_): # 각 선의 최대값 구하는 함수
    total = 0
 
    for i in range(100): # 가로 직선
        row = lst_sum(arr_[i][0:100])
        if row > total:
            total = row
 
    for j in range(100): # 세로 직선 
        column = lst_sum([row[j] for row in arr_])
        if column > total:
            total = column
 
    RL = 0
    for k in range(100): # 오른쪽 위에서 왼쪽 아래로 대각선
        RL += arr_[k][99-k]
    if RL > total:
        total = RL
 
    LR = 0
    for p in range(100): # 왼쪽 위에서 오른쪽 아래로 대각선
        LR += arr_[p][p]
    if LR > total:
        total = LR
 
    return total # 최대값 return
 
for _ in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{T} {line_sum(arr)}')
