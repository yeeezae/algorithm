#11508. 2+1 세일
#!/usr/bin/env python3
import sys
readl = sys.stdin.readline
if __name__ == "__main__":
    N = int(readl())
    dairy = []
    res = 0
    for i in range(N):
        dairy.append(int(readl()))
    dairy.sort(reverse=True)

    for i in range(N):
        if (i % 3 != 2):
            res += dairy[i]
    print(res)