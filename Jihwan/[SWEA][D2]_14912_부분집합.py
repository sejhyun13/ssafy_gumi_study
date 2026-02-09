"""
10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를 작성해보자.
부분집합의 합이 0인 것이 존재하면 1를 출력하고 그렇지 않으면 0를 출력한다.(단, 공집합은 제외)

[입력]
총 T개의 테스트 케이스가 주어지며, 각 테스트 케이스의 첫 번째 줄에는 
배열의 길이(N)가 주어진다. 그리고 다음 줄에 1차원 배열이 주어진다.
"""

def check_zero(lst): #  부분집합의 합 함수
    total = 0
    for num in lst:
        total += num
     
    if total == 0: # 부분집합의 합이 0이면
        return True 
    return False
 
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
 
    for i in range(1, 1<<N): # 1부터 부분집합 개수
        sub = [] # 임시 부분 집합
        for j in range(N): # 비트 비교
            if i & (1<<j): # i의 j번 비트가 1이면
                sub.append(arr[j]) # 임시 부분 집합 추가
        if sub: # 공집합이 아니라면
            if check_zero(sub): # 부분집합이 합이 0인지 check
                print(f'#{t}', 1) 
                break
    else: # 합이 0인 부분집합이 없이 for문 다 돌아가면
        print(f'#{t}', 0)