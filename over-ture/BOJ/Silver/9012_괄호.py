import sys
# PS는 '('와 ')'만으로 구성된 문자열
# 그 중 괄호의 모양이 바르게 구성된 문자열을 VPS라고 한다
t = int(sys.stdin.readline())

for _ in range(t):

    l = sys.stdin.readline()
    # VPS 체크 플래그
    flag = 0
    for i in l:
        if i == '(':
            flag += 1
        elif i == ')':
            flag -= 1
        # 플래그가 -1이 되는 순간 VPS 아님
        if flag < 0:
            break

    if flag == 0:
        print('YES')
    else:
        print('NO')




