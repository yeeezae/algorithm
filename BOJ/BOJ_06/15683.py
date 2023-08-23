#15683. 감시(CCTV)
#!/usr/bin/env python3
import sys
import copy
#sys.stdin = open("input.txt", "r")
N,M = map(int, input().split())
cctv =[] #cctv 종류, x좌표, y좌표
board=[] #사무실 정보

#cctv 방향 정보
mode = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[0,3]],
    [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
    [[0,1,2,3]],]
    
#북-동-남-서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#감시
def fill(board, mode, x, y):
    for i in mode:
    	#x,y겂을 넘겨주고 while문 시작
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            #범위를 넘어가면 중단
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break
            #벽이면 중단
            if board[nx][ny] == 6:
                break
            #감시 가능
            elif board[nx][ny] == 0:
                board[nx][ny] = 7
                
#탐색
def dfs(depth, board):
    global min_value #최소값
    if depth == len(cctv): #탐색완료
        count = 0
        for i in range(N):
            count += board[i].count(0)
        #최소값 업데이트
        min_value = min(min_value, count)
        return
    tmp = copy.deepcopy(board) #보드 복사
    cctv_num, x, y = cctv[depth] #탐색할 cctv
    for i in mode[cctv_num]: #cctv의 방향에 따라서
        fill(tmp,i,x,y) #감시시작
        dfs(depth+1, tmp) #재귀호출
        tmp = copy.deepcopy(board) #보드 초기화


if __name__ == "__main__":
    for i in range(N):
        data = list(map(int, input().split()))
        board.append(data)
        for j in range(M):
            if data[j] in [1,2,3,4,5]:
                cctv.append([data[j],i,j])
            
    min_value = int(1e9)
    dfs(0, board)
    print(min_value)