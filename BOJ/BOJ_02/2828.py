#2828. 사과담기게임
#!/usr/bin/env python3
import sys
readl = sys.stdin.readline
if __name__ == "__main__":
    N, M = map(int, readl().split())
    j = int(readl())
    now = 1
    apples = []
    cnt = 0
    for i in range(j):
        apples.append(int(input()))
    for i in range(len(apples)):
        if now <= apples[i] and now + (M-1) >= apples[i]:
            continue
        elif now > apples[i]:
            cnt += abs(apples[i] - now)
            now = apples[i]
        else:
            cnt += apples[i] - (M-1) - now
            now = apples[i] - (M-1)
    print(cnt)