#!/usr/bin/env python3
import sys
import queue
from collections import deque
maps =list()
visited =list()
dx = [ -1,1,0,0 ]
dy = [ 0,0,-1,1 ]

    
if __name__ == "__main__":
    N,M = map(int,input().split())
    for i in range(N):
        maps.append([])
        visited.append([])
        line= input()
        for j in range(len(line)):
            maps[i].append(int(line[j]))
            visited[i].append(0)
    
    #BFS
    q = deque()
    q.append((0,0,1))
    visited[0][0] = 1
    while q:
        nr, nc, cnt = q.popleft()
        if (nr == N-1) and (nc ==M-1):
            break
        for i in range(4):
            nxr = nr + dx[i]
            nxc = nc + dy[i]
            if (0 <= nxr < N ) and (0 <= nxc < M) and (visited[nxr][nxc] == 0) and (maps[nxr][nxc] == 1):
                visited[nxr][nxc] = 1
                q.append((nxr,nxc,cnt+1))
    print(cnt)