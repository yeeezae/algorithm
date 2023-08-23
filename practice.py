#!/usr/bin/env python3
import sys
import copy
sys.stdin = open("input.txt", "r")
N,M = map(int, input().split())
cctv =[]
board=[]
mode = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[0,3]],
    [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
    [[0,1,2,3]],]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def fill(board, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7
def dfs(depth, board):
    global min_value
    if depth == len(cctv):
        count = 0
        for i in range(N):
            count += board[i].count(0)
        min_value = min(min_value, count)
        return
    tmp = copy.deepcopy(board)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(tmp,i,x,y)
        dfs(depth+1, tmp)
        tmp = copy.deepcopy(board)


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
                