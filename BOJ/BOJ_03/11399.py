#11399. ATM
#!/usr/bin/env python3
import sys
readl = sys.stdin.readline
if __name__ == "__main__":
    N = int(readl())
    p = list(map(int, readl().split()))
    p.sort()

    res = 0
    prev = 0
    for i in range(N):
        prev += p[i]
        res += prev
    print(res)