#10971. 외판원 순회 2
#!/usr/bin/env python3
import sys
sys.stdin=open('input.txt', 'r')
MIN_CNT = 100000
N = int(input())
maps = list()
visited = [ 0 for i in range(N) ]
rec = [ 0 for i in range(N) ]
def dfs(idx, value):
    global MIN_CNT
    global res
    rec[idx] = value
    res = 0
    if (idx + 1 == N):
        for i in range(N-1):
            s = rec[i]
            e = rec[i+1]
            if maps[s][e] == 0:
                return
            res += maps[s][e]
        if maps[rec[N-1]][rec[0]] == 0:
            return
        res += maps[rec[N-1]][rec[0]]
        if MIN_CNT > res:
            MIN_CNT = res
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(idx+1, i)
            visited[i] = 0

if __name__ == '__main__':
    for i in range(N):
        maps.append(list(map(int,input().strip().split())))
    for i in range(N):
        if visited[i] == 0:
            visited[i] =1
            dfs(0,i)
            visited[i] =0
    print(MIN_CNT)