#!/usr/bin/env python3
import sys

nrf = [0,1,0,-1]
ncf = [1,0,-1,0]
maps = list()
visited = list()
def dfs(r, c, d, v):
    print("-------")
    for i in range(len(visited)):
        print(visited[i])
    print("-------")
    cnt = 0
    for i in range(4):
        nr = r + nrf[i]
        nc = c + ncf[i]
        if (0 <= nr < N) and (0 <= nc < N) and (visited[nr][nc] >= 1):
            cnt +=1
        if cnt == 4:
            return
    nr = r + nrf[d]
    nc = c + ncf[d]
    if (0 <= nr < N) and (0 <= nc < N) and (maps[nr][nc] == 0) and (visited[nr][nc] == 0):
        visited[nr][nc] = v
        dfs(nr,nc,d, v+1)
    else:
        if d + 1 >= 4:
            d = 0
        else:
            d+=1
        nr = r + nrf[d]
        nc = c + ncf[d]
        if (0 <= nr < N) and (0 <= nc < N) and (maps[nr][nc] == 0) and (visited[nr][nc] == 0):
            visited[nr][nc] = v
            dfs(nr,nc,d, v+1)
    

if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        maps.append([])
        visited.append([])
        for j in range(N):
            maps[i].append(0)
            visited[i].append(0)
    visited[0][0]=1
    dfs(0,0,0,2) # 0 -->