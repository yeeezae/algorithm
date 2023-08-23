#1012. 유기농 배추
#!/usr/bin/env python3
import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10000) #dfs시 런타임 에러 -> bfs로 해결 가능

T = int(input())
maps=list()
visited=list()

nrf = [1,-1,0,0]
ncf = [0,0,1,-1]
def dfs(r,c):
    for i in range(4):
        nr = r + nrf[i]
        nc = c + ncf[i]
        if (0 <= nr < M) and (0 <= nc < N) and (visited[nr][nc] == 0) and (maps[nr][nc] == 1):
            visited[nr][nc] = 1
            dfs(nr,nc)
if __name__ == "__main__":
    for test_case in range(1, T+1):
        M, N, K = map(int, input().split())
        cnt = 0
        maps.clear()
        visited.clear()
        for i in range(M):
            maps.append([])
            visited.append([])
            for j in range(N):
                maps[i].append(0)
                visited[i].append(0)

        for i in range(K):
            X,Y =map(int,input().split())
            maps[X][Y] = 1
        
        for i in range(M):
            for j in range(N):
                if visited[i][j] == 0 and maps[i][j] ==1:
                    visited[i][j] = 1
                    cnt +=1
                    dfs(i,j)
        print(cnt)