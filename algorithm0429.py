nrf = [1, -1, 0, 0]
ncf = [0, 0, 1, -1]
def dfs(r, c):
    for i in range(4):
        nr = r + nrf[i]
        nc = c + ncf[i]
        if(0 <= nr < N) and (0 <= nc < N) and (maps[nr][nc] == 1) and (visited[nr][nc] == 0):
            visited[nr][nc] = 1
            dfs(nr, nc)


if __name__ == '__main__':
    N= int(input)
    maps= list()
    visited= list()
    for i in range(N):
        maps.append([])
        visited.append([])
        line= input()
        for j in range(len(line)):
            maps[i].append(int(line[j]))
            visited[i].append(0)
    
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 0 and visited[i][j] ==0:
                visited[i][j] ==1
                dfs(i,j);