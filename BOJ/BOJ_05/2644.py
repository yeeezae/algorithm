#2644. 촌수계산
#!/usr/bin/env python3
import sys
readl = sys.stdin.readline
from collections import deque

    
if __name__ == "__main__":
    n = int(input())
    A,B = map(int,input().split())
    m = int(input())
    family =[ [] for _ in range(n+1) ]
    res=-1
    visited = [False] * (n+1)
    for i in range(m):
        x,y = map(int,input().split())
        family[x].append(y)
        family[y].append(x)
    
    q = deque()
    q.append((A,0))
    visited[0] = True
    while q:
        node, cnt = q.popleft()
        if node == B:
            res = cnt
            break
        for i in family[node]:
            if visited[i] == False:
                visited[i] = True
                q.append((i, cnt+1))
    print(res)