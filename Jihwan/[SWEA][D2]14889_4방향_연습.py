"""
5x5 2차 배열에 무작위로 25개의 숫자로 초기화 한 후 25개의 각 요소에 대해서 
그 요소와 이웃한 요소와의 차의 절대값을 구하시오.
예를 들어 아래 그림에서 7 값의 이웃한 값은 2, 6, 8, 12 이며 차의 절대값의 합은 12 이다.
  | 2 – 7 | + | 6 – 7 | + | 8 – 7 | + | 12 – 7 | = 12

25개의 요소에 대해서 모두 조사하여 총합을 구하시오.
벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주의하시오. 예를 들어 [0][0]은 이웃한 요소가 2개이다.

[입력]
첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 
각 테스트 케이스는 다음과 같이 구성되었다.
- 첫 번째 줄에 배열의 크기 N이 주어진다. 
- 두 번째 줄 부터  N X N 개의 배열이 주어진다.
"""
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    dx = [0, 1, 0, -1] # 북 동 남 서 (시계방향)
    dy = [1, 0, -1, 0]
 
    def abs(num): # 절대값 만들기 함수
        if num < 0:
            return -1 * num
        return num
 
    total = 0
    for i in range(N): # row
        for j in range(N): # column
            for xy_index in range(4): # dx, dy의 시계방향 인덱스
                middle = arr[i][j] # 중심 요소
                ix = i + dx[xy_index] # 중심 요소 + dx 
                jy = j + dy[xy_index] # 중심 요소 + dy
                if 0 <= ix < N and 0 <= jy < N: # 방향 인덱스가 범위 안이면:
                    total += abs(middle - arr[ix][jy]) # 중심 요소 - 이웃 요소의 절대값
 
    print(f'#{t} {total}')