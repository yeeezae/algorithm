#9663. N-Queen
#!/usr/bin/env python3
import sys
def dfs(n):
    if n == N: # 마지막까지 탐색 완료
        global count # 전역변수 설정
        count += 1 # 값 증가
    else:
        for i in range(N):
            if visited[i]:
                continue
            board[n] = i # (n, i)에 퀸 올리기
            if check(n): # 퀸 놓기 조건에 맞다면
                visited[i] = True
                dfs(n+1) # 다음 행으로 넘어가긴
                visited[i] = False

def check(n):
    for i in range(n):
        # 이미 놓여진 퀸과 같은 열이거나 대각선 상에 있는지 확인
        # (행끼리의 차 == 열끼리 차의 절대값)이 True면 대각선 상에 있는 것임
        if (board[n] == board[i]) or (n - i == abs(board[n] - board[i])):
            return False
    return True

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    count = 0
    board = [0 for _ in range(N)] # 인덱스 번호 == 행, 인덱스 값 == 열
    visited = [False for _ in range(N)]

    dfs(0)
    print(count)