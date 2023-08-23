#20300. 서강근육맨
#!/usr/bin/env python3
import sys
readl = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    muscle = list(map(int, input().split()))
    muscle.sort()
    muscle_res=[]
    if N % 2 == 0:
        min_res = muscle[0] + muscle[N-1]
        muscle_res.append(min_res)
        for i in range(N//2):
            res = 0 
            res += muscle[i] + muscle[N-i-1]
            muscle_res.append(res)
    elif N %2 ==1:
        min_res = muscle[N-1]
        muscle_res.append(min_res)
        for i in range(N//2):
            res = 0 
            res += muscle[i] + muscle[N-i-2]
            muscle_res.append(res)
    res = max(muscle_res)
    print(res)