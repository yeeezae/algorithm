#!/usr/bin/env python3
import sys
sys.stdin = open("input.txt", "r")
nrf = [1,-1,0,0]
ncf = [0,0,1,-1]
cnt = 0

def dfs(r, c, danji_cnt):
    print('-------------------')
    for i in range(N):
        print(visited[i])
    print('-------------------')
    for i in range(4):
        nr = r + nrf[i]
        nc = c + ncf[i]
        if (0 <= nr < N) and (0 <= nc < N) and (maps[nr][nc] == 1) and (visited[nr][nc] == 0):
            visited[nr][nc] = cnt
            danji_cnt=dfs(nr,nc,danji_cnt+1)
    return danji_cnt

if __name__ == '__main__':
    N = int(input())
    #maps =[ list(input()) for _ in range(n)]
    maps = list()
    visited = list()
    for i in range(N):
        maps.append([])
        visited.append([])
        line = input()
        for j in range(len(line)):
            maps[i].append(int(line[j]))
            visited[i].append(0)
    print('-------------------')
    for i in range(N):
        print(visited[i])
    print('-------------------')
    house= []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                visited[i][j] = cnt
                danji_cnt=0
                danji_cnt=dfs(i,j,danji_cnt+1)
                house.append(danji_cnt)

    print('-------------------')
    for i in range(N):
        print(visited[i])
    print('-------------------')
    print(house)
