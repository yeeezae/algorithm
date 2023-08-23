#1012. 유기농 배추(BFS)
#!/usr/bin/env python3
import sys
import queue
from collections import deque
T=int(input())
maps =list()
visited =list()
dx = [ -1,1,0,0 ]
dy = [ 0,0,-1,1 ]
def bfs(x,y):
    global res
    q =deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < M) and (0<=ny<N) and (visited[nx][ny] == 0) and (maps[nx][ny] == 1):
                visited[nx][ny] = 1
                q.append((nx,ny))
                
if __name__ == "__main__":
    for test_case in range(1, T+1):
        M,N,K = map(int, input().split())
        maps.clear()
        visited.clear()
        for i in range(M):
            maps.append([])
            visited.append([])
            for j in range(N):
                maps[i].append(0)
                visited[i].append(0)

        for i in range(K):
            X,Y = map(int, input().split())
            maps[X][Y] = 1
        cnt = 0
        for i in range(M):
            for j in range(N):
                if visited[i][j] == 0 and maps[i][j] ==1:
                    visited[i][j] = 1
                    bfs(i,j)
                    cnt +=1
        print(cnt)