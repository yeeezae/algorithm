#10971. 외판원 순회 2
#!/usr/bin/env python3
import sys
sys.stdin=open('input.txt', 'r')
MIN_CNT = sys.maxsize
def dfs(start, now, value, cnt):
    global MIN_CNT
    if (cnt == N):
    	# 0->1 1->2 2->3 3->0 다시 처음으로 돌아가는 시간도 합에 추가
        if maps[now][start]:
            value += maps[now][start]
            if MIN_CNT > value:
                MIN_CNT = value
        return
        
    if value > MIN_CNT:
        return

    for i in range(N):
        if visited[i] == 0 and maps[now][i]: #현재 노드에 있으면
            visited[i] = 1
            # 0->1 1->2 2->3
            dfs(start, i, value+maps[now][i], cnt+1 )
            visited[i]=0

if __name__ == '__main__':
    N = int(input())
    maps = list()
    for i in range(N):
        maps.append(list(map(int,input().strip().split())))
    visited = [ 0 for i in range(N) ]

    for i in range(N):
        if visited[i] == 0:
            visited[i] =1
            #자기자신부터 출발
            dfs(i,i,0,1)
            visited[i] =0
    print(MIN_CNT)